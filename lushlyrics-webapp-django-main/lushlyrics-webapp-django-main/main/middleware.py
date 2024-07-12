from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of allowed paths for unauthenticated users
        allowed_paths = [
            settings.LOGIN_URL, 
            reverse('register'),
            reverse('password_reset'),
            reverse('password_reset_done'),
            reverse('password_reset_confirm', kwargs={'uidb64': 'dummy-uid', 'token': 'dummy-token'}),
            reverse('password_reset_complete'),
        ]
        
        if not request.user.is_authenticated and not any(request.path.startswith(path) for path in allowed_paths):
            # Redirect to login page
            return redirect(settings.LOGIN_URL)
        
        response = self.get_response(request)
        return response
