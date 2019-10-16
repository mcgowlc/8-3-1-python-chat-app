from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from models import Profile


class SignUpView(generic.CreateView):
   form_class = UserCreationForm
   template_name = 'signup.html'
   success_url = reverse_lazy('login')


class LoginView(CreateView):
   form_class = UserCreationForm
   template_name = 'login.html'
   success_url = reverse_lazy('home')m

 class ProfileCreateView(generic.CreateView):
     model = Profile
     template_name = 'profile'
