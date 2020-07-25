from django.urls import path
from app.core.views import MainPageView, SignUpView, LoginView, LogoutView


urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
