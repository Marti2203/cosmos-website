from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template
from mysite.services import FacebookService


def display_album(request, album_id):
    """
    Retrieves images from facebook album.
    If album does not exist, the user is redirected to the albums page (/association/photos/)
    """

    (success, album) = FacebookService.get_photos(album_id)
    if not success:
        return redirect('/association/photos/')

    template = get_template("/widgets/gallery_album.html")
    html = template.render({'album': album}, request)

    return HttpResponse(html)
