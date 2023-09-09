from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import SigninForm
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='pages/signin.html', authentication_form=SigninForm), name='signin'),
]
