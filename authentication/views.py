from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .models import UserProfile
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView 
from django.contrib.auth import logout 
# Create your views here.

class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = 'login'
# The UserProfile model is a custom model linked to the User model via a OneToOneField. This line creates a new UserProfile instance for the newly registered user (user). The UserProfile is used to store additional information about the user, such as their balance, that isn't included in the default User model.
    def form_valid(self,form):
        user = form.save()
        UserProfile.objects.create(user = user)
        return redirect(self.success_url)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context

class UserLoginView(LoginView):
    template_name = 'registration.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('home') 


