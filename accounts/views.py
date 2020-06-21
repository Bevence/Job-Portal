from django.shortcuts import render, HttpResponse
from django.views import View
from accounts.forms import UserRegistrationForm


# Create your views here.


class UserRegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        template_name = "accounts/signup.html"
        return render(request, template_name, {"form" : form})
