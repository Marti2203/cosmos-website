from .models import Door

def door_status_processor(request):
    door_status = Door.objects.get(id=1).is_open           
    return {'door_status': door_status}