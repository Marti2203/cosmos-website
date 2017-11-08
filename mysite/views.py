from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

# TODO: Proper django form
def update_profile(request):
	print(request.method)
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
