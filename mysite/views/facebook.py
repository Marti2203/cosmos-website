from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template
import requests
from ..settings import API_VERSION, TOKEN


def display_album(request):
    """
    Retrieves images from facebook album.
    If album does not exist, the user is redirected to the albums page (/association/photos/)

    :param request:
    :return:
    """

    # Get album id. Url ends with /, so we split by '/' and get the second to last.
    album_id = request.get_full_path().split("/")[-2]

    # TODO put in a service
    r = requests.get(
        'https://graph.facebook.com/%s/%s/?fields=photos.limit(1000){images},description,name&access_token=%s' % (
            API_VERSION, album_id, TOKEN))
    if r.status_code != requests.codes.ok:
        return redirect('/association/photos/')

    template = get_template("/widgets/gallery_album.html")
    html = template.render({'album': r.json()}, request)

    return HttpResponse(html)
