from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.template.loader import get_template
from mysite.exceptions import *
from mysite.settings import DEFAULT_FROM_EMAIL


# TODO figure out if this is necessary
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

    fields = ['department', 'program', 'nationality',
              'tue_id', 'phone_nr', 'gender', 'card_number']
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

    fields = ['department', 'program', 'nationality',
              'tue_id', 'phone_nr', 'gender', 'card_number']
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

    user.profile.member_type = 'MEMBER'
    user.save()

    message = \
"""Dear {},

Your information has been verified and your account is now activated.
               
Best regards,
The Cosmos Website Committee 
""".format(user.first_name)

    return process_request(user,'MEMBER',message)

# For now it just makes the user's member_type "rejected". Will consider deleting from DB


def reject_request(request):
    try:
        user = get_admin_user(request)
    except UserException:
        return redirect('/requests')

    message = \
"""Dear {},

We regret to inform you that after reviewing your information, your membership request has been rejected.
If you would like to reach us,you can do so sending an email to cosmos@tue.nl. 

Best regards,
The Cosmos Website Committee
""".format(user.first_name)

    return process_request(user, 'Rejected', message)


def process_request(user, member_type, message):
    user.profile.member_type = member_type
    user.save()
    send_mail('Your account has been verified',
              message, DEFAULT_FROM_EMAIL, [user.email])
    return redirect('/requests')
