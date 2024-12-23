from django.http import HttpResponse
from django.urls import reverse


def index(request):
    signup_url = reverse("account_signup")
    return HttpResponse(f'<a href="{signup_url}">Hello, please Sign Up here!</a>')
