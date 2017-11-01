from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

def update_profile(request):
    if request.method == 'POST':
        user_id = int(request.user.id)
        user = User.objects.get(id=user_id)
        email = request.POST['email']
        user.username = email
        user.email = email
        user.save()
    return redirect('/activities')