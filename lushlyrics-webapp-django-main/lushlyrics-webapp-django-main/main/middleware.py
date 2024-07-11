from typing import Any
from django.conf import settings
from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in [settings.LOGIN_URL, '/signup/']:  # Allow access to login and signup pages
            return redirect(settings.LOGIN_URL)
        response = self.get_response(request)
        return response