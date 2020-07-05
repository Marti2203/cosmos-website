import requests
import os
if os.environ["DJANGO_SETTINGS_MODULE"] == "mysite.settings":
    from mysite.settings import FACEBOOK_API_VERSION, COSMOS_FACEBOOK_ACCOUNT_ID, FACEBOOK_API_TOKEN
else:
    from mysite.settings_pr import API_VERSION, COSMOS_ID, TOKEN


class FacebookService:
    @staticmethod
    def get_albums(maximum=500):
        r = requests.get(
            'https://graph.facebook.com/{}/{}/?fields=albums.limit({}){{cover_photo{{images}},name,photo_count}}&access_token={}'.format(
                FACEBOOK_API_VERSION, COSMOS_FACEBOOK_ACCOUNT_ID, maximum, FACEBOOK_API_TOKEN))
        return (r.status_code == requests.codes.ok, r.json() if r.status_code == requests.code.ok else None )

    @staticmethod
    def get_future_events():
        r = requests.get(
            'https://graph.facebook.com/{}/{}/?fields=events.time_filter(upcoming){{cover,name,start_time,description}}&access_token={}'.format(FACEBOOK_API_VERSION, COSMOS_FACEBOOK_ACCOUNT_ID, FACEBOOK_API_TOKEN)).json()
        return (r.status_code == requests.codes.ok, r.json() if r.status_code == requests.code.ok else None )

    @staticmethod
    def get_past_events(maximum=16):
        r = requests.get(
            'https://graph.facebook.com/{}/{}/?fields=events.time_filter(past).limit({}){{cover,name,start_time,description}}&access_token={}'.format(
                FACEBOOK_API_VERSION, COSMOS_FACEBOOK_ACCOUNT_ID, maximum, FACEBOOK_API_TOKEN)).json()
        return (r.status_code == requests.codes.ok, r.json() if r.status_code == requests.code.ok else None )

    @staticmethod
    def get_photos(album_id, maximum=1000):
        r = requests.get(
            'https://graph.facebook.com/{}/{}/?fields=photos.limit({}){{images}},description,name&access_token={}'.format(
                FACEBOOK_API_VERSION, COSMOS_FACEBOOK_ACCOUNT_ID, maximum, album_id, FACEBOOK_API_TOKEN)).json()
        return (r.status_code == requests.codes.ok, r.json() if r.status_code == requests.code.ok else None )
