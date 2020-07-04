from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.template.loader import get_template
from .models import Token, Pi, Door
from mysite.exceptions import *
# from django.template import RequestContext
import requests
import os

# Check if in production environment or not
if os.environ["DJANGO_SETTINGS_MODULE"] == "mysite.settings":
    from mysite.settings import TOKEN, API_VERSION, DEFAULT_FROM_EMAIL
else:
    from mysite.settings_pr import EMAIL_HOST_USER, DEFAULT_FROM_EMAIL, TOKEN, API_VERSION


def set_values(object, values, fields):
    for field in fields:
        setattr(object, field, values[field])
    return object


# TODO: Proper django form
def update_profile(request):
    if request.method != 'POST' or not request.user.is_authenticated:
        return redirect('/login')

    email = request.POST['email']
    if request.user.email != email and User.objects.filter(username=email).exists():
        return redirect('/profile?updated=false&error=email-exists')

    user = User.objects.get(id=int(request.user.id))

    fields = ['first_name', 'last_name', 'email']
    user = set_values(user, request.POST, fields)
    user.username = email

    fields = ['department', 'program', 'nationality', 'tue_id', 'phone_nr', 'gender', 'card_number']
    user.profile = set_values(user.profile, request.POST, fields)

    user.save()
    return redirect('/profile?updated=true')


def create_member(request):
    if request.method != 'POST':
        # If function triggered NOT by the form, redirect to webpage
        return redirect('/create-member')

    email = request.POST['email']
    if User.objects.filter(username=email).exists():
        return redirect('/join?joined=false&error=email-exists')
    if request.POST['password'] != request.POST['password-confirm']:
        return redirect('/join?joined=false&error=password')

    user = User.objects.create_user(email)

    fields = ['first_name', 'last_name']
    user = set_values(user, request.POST, fields)
    user.email = email

    fields = ['department', 'program', 'nationality', 'tue_id', 'phone_nr', 'gender', 'card_number']
    user.profile = set_values(user.profile, request.POST, fields)

    user.password = make_password(request.POST['password'])
    user.profile.key_access = 'No'
    user.profile.member_type = 'Pending'

    user.save()

    message = "Dear " + user.first_name + \
              ", \n \n Your account has been created successfully, your information " \
              "will be validated as soon as possible by our board members. As soon as " \
              "your information is verified, you will receive an e-mail from us. \n \n " \
 \
        # Email the user that just signed up
    send_mail(
        'Signup Confirmation',
        message,
        DEFAULT_FROM_EMAIL,
        [user.email],
        # fail_silently=False,
    )

    message = "Someone just signed up, please go to www.cosmostue.nl/requests to review his request."

    # Email internal affairs to let them know someone signed up
    send_mail(
        'Someone just signed up',
        message,
        DEFAULT_FROM_EMAIL,
        ['internal.cosmos@tue.nl'],
    )

    return redirect('/join?joined=true')


# TODO unused?
def list_requests(request):
    if request.user.is_authenticated and request.user.is_staff:
        join_requests = User.objects.filter(profile__member_type='Pending')
        template = get_template("/request-list.html")
        html = template.render({"requests": join_requests}, request)

        return HttpResponse(html)
    return redirect('/login')


def get_admin_user(request):
    if not request.user.is_authenticated:
        raise UserNotLoggedInException

    if not request.user.is_staff:
        raise UserNotAdminException

    id = request.GET.get('id')
    if id is None:
        raise UserNotAdminException

    try:
        user = User.objects.get(id=id)
        return user
    except User.DoesNotExist:
        raise UserNotAdminException


def accept_request(request):
    try:
        user = get_admin_user(request)
    except UserException:
        return redirect('/requests')

    user = User.objects.get(id=id)
    user.profile.member_type = 'MEMBER'
    user.save()

    message = "Dear " + user.first_name + \
              ", \n \n Your information has been verified and your account is now " \
              "activated. \n \n Best regards, \n The Cosmos Website Committee \n "

    # Email the user that just got accepted
    send_mail(
        'Your account has been verified',
        message,
        DEFAULT_FROM_EMAIL,
        [user.email],
    )

    return redirect('/requests')


# For now it just makes the user's member_type "rejected". Will consider deleting from DB
def reject_request(request):
    try:
        user = get_admin_user(request)
    except UserException:
        return redirect('/requests')

    user.profile.member_type = 'Rejected'
    user.save()

    message = "Dear " + user.first_name + \
              ", \n \n We regret to inform you that after reviewing your information, " \
              "your membership request has been rejected. If you would like to reach us, " \
              "you can do so sending an email to cosmos@tue.nl. \n \n " \
              "Best regards, \n The Cosmos Website Committee \n "

    # Email the user that just got rejected
    send_mail(
        'Your account has been verified',
        message,
        DEFAULT_FROM_EMAIL,
        [user.email],
    )

    return redirect('/requests')


def display_album(request):
    """
    Retrieves images from facebook album.
    If album does not exist, the user is redirected to the albums page (/association/photos/)

    :param request:
    :return:
    """

    # Get album id. Url ends with /, so we split by '/' and get the second to last.
    album_id = request.get_full_path().split("/")[-2]

    # TODO put in a service
    r = requests.get(
        'https://graph.facebook.com/%s/%s/?fields=photos.limit(1000){images},description,name&access_token=%s' % (
            API_VERSION, album_id, TOKEN))
    if r.status_code != requests.codes.ok:
        return redirect('/association/photos/')

    template = get_template("/widgets/gallery_album.html")
    html = template.render({'album': r.json()}, request)

    return HttpResponse(html)


def display_door_status(request):
    is_door_open = Door.objects.get(id=1).is_open

    status = 'open' if is_door_open else 'closed'
    return HttpResponse(status)


def update_door_status(request):
    try:
        token = request.GET.get('access_token')
        status = 1 if request.GET.get('status') == 'open' else 0

        if Token.objects.filter(token=token).exists():
            door = Door.objects.get(id=1)
            door.is_open = status  # change field
            door.save()
            return HttpResponse("Updated door status")
        return HttpResponse("Invalid token", status=401)
    # TODO change exception to something specific
    except Exception as e:
        return HttpResponse("There was an error updating the door status", status=500)


def update_pi_ip(request):
    try:
        token = request.GET.get('access_token')
        ip = request.GET.get('ip')

        if Token.objects.filter(token=token).exists():
            pi = Pi.objects.get(id=1)
            pi.ip = ip  # change field
            pi.save()
            return HttpResponse("Updated Pi IP")
        return HttpResponse("Invalid token", status=401)
    # TODO change exception to something specific
    except Exception as e:
        return HttpResponse("There was an error updating the IP", status=500)
