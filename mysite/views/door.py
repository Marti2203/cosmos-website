from django.http import HttpResponse
from ..models import Token, Pi, Door


def display_status(request):
    is_door_open = Door.objects.get(id=1).is_open

    status = 'open' if is_door_open else 'closed'
    return HttpResponse(status)


def update_status(request):
    try:
        token = request.GET.get('access_token')
        status = 1 if request.GET.get('status') == 'open' else 0

        if Token.objects.filter(token=token).exists():
            door = Door.objects.get(id=1)
            door.is_open = status  # change field
            door.save()
            return HttpResponse("Updated door status")
        return HttpResponse("Invalid token", status=401)
    # TODO change exception to something specific
    except Exception as e:
        return HttpResponse("There was an error updating the door status", status=500)


def update_pi_ip(request):
    try:
        token = request.GET.get('access_token')
        ip = request.GET.get('ip')

        if Token.objects.filter(token=token).exists():
            pi = Pi.objects.get(id=1)
            pi.ip = ip  # change field
            pi.save()
            return HttpResponse("Updated Pi IP")
        return HttpResponse("Invalid token", status=401)
    # TODO change exception to something specific
    except Exception as e:
        return HttpResponse("There was an error updating the IP", status=500)
