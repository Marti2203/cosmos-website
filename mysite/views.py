from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

# TODO: Proper django form
def update_profile(request):
    if request.method == 'POST':
    	if request.user.is_authenticated():
	        user = User.objects.get(id=int(request.user.id))
	        email = request.POST['email']
	        user.username = email
	        user.email = email
	        user.save()
	        return redirect('/profile?updated=true')
    return redirect('/login')