from django.http import HttpResponseRedirect
from django.conf import settings

class LoginRequired(object):
    def __init__(self):
        self.login_url = getattr(settings, 'LOGIN_URL', '/login/')

    def process_request(self, request):
        """
        Ensure that user is authenticated when accessing a Django-CMS page
        """
        if getattr(request, 'current_page', None) and not request.user.is_authenticated() and request.path[:7] == "members":
            return HttpResponseRedirect("%s?next=%s" % (self.login_url, request.path))
