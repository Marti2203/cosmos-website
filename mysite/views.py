from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import RequestContext

def set_values(object, values, fields):
	for field in fields:
		setattr(object, field, values[field])
	return object

# TODO: Proper django form
def update_profile(request):
	if request.method == 'POST':
		if request.user.is_authenticated():
			email = request.POST['email']
			if User.objects.filter(username=email).exists():
				return redirect('/profile?updated=false&error=email-exists')

			user = User.objects.get(id=int(request.user.id))

			fields = ['first_name', 'last_name', 'email']
			user = set_values(user, request.POST, fields)
			user.username = email

			fields = ['department', 'program', 'nationality', 'tue_id', 'phone_nr', 'gender', 'card_number']
			user.profile = set_values(user.profile, request.POST, fields)

			user.save()
			return redirect('/profile?updated=true')
	return redirect('/login')

def create_member(request):
	if request.method == 'POST':
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
		return redirect('/join?joined=true')

def list_requests(request):
	if request.user.is_authenticated and request.user.is_staff:

		join_requests = User.objects.filter(profile__member_type='Pending')
		request_context = RequestContext(request, {"requests": join_requests})

		return render_to_response('request-list.html', request_context)
	return redirect('/login')

def accept_request(request):
	if request.user.is_authenticated and request.user.is_staff:

		id = request.GET.get('id')
		if id is None:
			return redirect('/requests')
		try:
			user = User.objects.get(id=id)
		except User.DoesNotExist:
			return redirect('/requests')

		user.profile.member_type = 'Member'
		user.save()

		return redirect('/requests')
	return redirect('/login')

# For now it just makes the user's member_type "rejected". Will consider deleting from DB
def reject_request(request):
	if request.user.is_authenticated and request.user.is_staff:

		id = request.GET.get('id')
		if id is None:
			return redirect('/requests')
		try:
			user = User.objects.get(id=id)
		except User.DoesNotExist:
			return redirect('/requests')

		user.profile.member_type = 'Rejected'
		user.save()

		return redirect('/requests')
	return redirect('/login')