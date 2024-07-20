from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
# Create your views here.

class SignupView(CreateView): #signup hiya s'insecription
    form_class = UserCreationForm    #hadi la forme(bel html w css) ta3 insecription wajda
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs) :  #The get() method is used to handle HTTP GET requests
        if self.request.user.is_authenticated : # checks if the user making the request is authenticated or logged in  The is_authenticated attribute returns True if the user is authenticated; otherwise, it returns False.
            return redirect('notes.list')  #If the user is authenticated, the function redirects them to the 'notes.list' URL using the redirect() function
        return super().get(request, *args, **kwargs)  #If the user is not authenticated, the function executes the line return super().get(request, *args, **kwargs). Here's what it does: super() is used to call the parent 
                                                      #class's implementation of the get() method. The super().get(request, *args, **kwargs) line passes the request, *args, and **kwargs parameters to the parent class's get() method, allowing the parent class to perform its logic and return an HTTP response.
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
class LoginInterfaceView(LoginView) : 
    template_name = 'home/login.html'

class HomeView(TemplateView): #li dakhel ala9was HomeView tewret mn 3ndha
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
