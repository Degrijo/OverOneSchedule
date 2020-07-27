from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.views import View

from app.core.forms import SignUpForm, LoginForm


#  TODO: RestorePasswordView, Email mailing, Telegram mailing

class MainPageView(TemplateView):
    template_name = 'core/main_page.html'


class SignUpView(FormView):
    template_name = 'core/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    extra_context = {'login_url': reverse_lazy('login')}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'core/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')
    extra_context = {'signup_url': reverse_lazy('signup')}

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('home')


class ProfileView(TemplateView):
    template_name = 'core/profile.html'
