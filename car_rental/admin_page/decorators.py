from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
from functools import wraps

def staff_required(view_func):
    """
    allows access only to admin(staff) users.
    redirecrs non-authenticated and non-admin users to login page.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)

        messages.error(request, "You are not authorized to access admin panel.")
        return redirect(settings.LOGIN_URL)

    return wrapper