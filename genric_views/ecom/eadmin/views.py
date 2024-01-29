from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm

class CustomLogoutView(LoginView):
    next_page = reverse_lazy('login')

class CustomRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    model = User
    success_url = reverse_lazy('login')