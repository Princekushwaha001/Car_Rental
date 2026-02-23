from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .models import User
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "accounts/register.html"
    success_url = "/"

class UnifiedLoginView(LoginView):
    template_name = "accounts/login.html"

    def form_valid(self, form):
        user = form.get_user()
        login_type = self.request.POST.get("login_type")

        # If admin selected
        if login_type == "admin":
            if not user.is_staff:
                messages.error(self.request, "Admin access only.")
                return redirect("login")

        # Optional: block staff from user tab
        if login_type == "user":
            if user.is_staff:
                messages.error(self.request, "Please use admin login.")
                return redirect("login")

        return super().form_valid(form)

    def get_success_url(self):
        user = self.request.user
        if user.is_staff:
            return "/admin_page/list_car/"
        return "/"