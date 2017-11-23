from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

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