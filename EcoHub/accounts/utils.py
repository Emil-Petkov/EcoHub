from django.conf import settings
from urllib.parse import urlencode

def get_google_maps_url(address):
    base_url = "https://www.google.com/maps/embed/v1/place"
    params = {
        "key": settings.GOOGLE_MAPS_API_KEY,
        "q": address,
    }
    return f"{base_url}?{urlencode(params)}"
