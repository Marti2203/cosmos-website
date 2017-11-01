from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

def update_profile(request):
    if request.method == 'POST':
        user_id = int(request.POST['id'])
        user = User.objects.get(id=user_id)

        first_name = request.POST['first_name']
        user.first_name = first_name

        last_name = request.POST['last_name']
        user.last_name = last_name

        email = request.POST['email']
        user.email = email

        department = request.POST['department']
        user.profile.department = department

        user.save()
    return redirect('/profile')
