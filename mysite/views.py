from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# TODO: Proper django form
def update_profile(request):
	if request.method == 'POST':
		if request.user.is_authenticated():
			user = User.objects.get(id=int(request.user.id))

			first_name = request.POST['first_name']
			user.first_name = first_name

			last_name = request.POST['last_name']
			user.last_name = last_name

			email = request.POST['email']
			user.email = email
			user.username = email

			department = request.POST['department']
			user.profile.department = department

			program = request.POST['program']
			user.profile.program = program

			nationality = request.POST['nationality']
			user.profile.nationality = nationality

			tue_id = request.POST['tue_id']
			user.profile.tue_id = tue_id

			phone_nr = request.POST['phone_nr']
			user.profile.phone_nr = phone_nr

			gender = request.POST['gender']
			user.profile.gender = gender

			card_number = request.POST['card_number']
			user.profile.card_number = card_number

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
		first_name = request.POST['first_name']
		user.first_name = first_name

		last_name = request.POST['last_name']
		user.last_name = last_name

		user.email = email

		department = request.POST['department']
		user.profile.department = department

		program = request.POST['program']
		user.profile.program = program

		nationality = request.POST['nationality']
		user.profile.nationality = nationality

		tue_id = request.POST['tue_id']
		user.profile.tue_id = tue_id

		phone_nr = request.POST['phone_nr']
		user.profile.phone_nr = phone_nr

		gender = request.POST['gender']
		user.profile.gender = gender

		card_number = request.POST['card_number']
		user.profile.card_number = card_number

		user.password = make_password(request.POST['password'])
		user.profile.key_access = 'No'
		user.profile.member_type = 'Pending'

		user.save()
		return redirect('/join?joined=true')