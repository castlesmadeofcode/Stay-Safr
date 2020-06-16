from django.urls import path, include
from .views import *

app_name = "capstoneapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home'),
]