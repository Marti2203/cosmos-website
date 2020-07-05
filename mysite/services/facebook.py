import requests
import os
if os.environ["DJANGO_SETTINGS_MODULE"] == "mysite.settings":
    from mysite.settings import FACEBOOK_API_VERSION, COSMOS_FACEBOOK_ACCOUNT_ID, FACEBOOK_API_TOKEN
else:
    from mysite.settings_pr import API_VERSION, COSMOS_ID, TOKEN


class FacebookService:
    @staticmethod
    def get_albums(maximum=500):
        return requests.get(
            'https://graph.facebook.com/{}/{}/?fields=albums.limit({}){{cover_photo{{images}},name,photo_count}}&access_token={}'.format(
                FACEBOOK_API_VERSION, COSMOS_FACEBOOK_ACCOUNT_ID, maximum, FACEBOOK_API_TOKEN)).json()

    @staticmethod
    def get_future_events():
        return requests.get(
            'https://graph.facebook.com/{}/{}/?fields=events.time_filter(upcoming){{cover,name,start_time,description}}&access_token={}'.format(FACEBOOK_API_VERSION, COSMOS_FACEBOOK_ACCOUNT_ID, FACEBOOK_API_TOKEN)).json()

    @staticmethod
    def get_past_events(maximum=16):
        return requests.get(
            'https://graph.facebook.com/{}/{}/?fields=events.time_filter(past).limit({}){{cover,name,start_time,description}}&access_token={}'.format(
                FACEBOOK_API_VERSION, COSMOS_FACEBOOK_ACCOUNT_ID, maximum, FACEBOOK_API_TOKEN)).json()
