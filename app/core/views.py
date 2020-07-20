from django.contrib.auth import get_user_model, login, logout
from django.views.generic import TemplateView, FormView
from app.core.forms import SignUpForm


class MainPageView(TemplateView):
    template_name = 'core/main_page.html'


class SignUpView(FormView):
    template_name = 'core/signup.html'
    form_class = SignUpForm
