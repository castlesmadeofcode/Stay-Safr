from django.urls import path, include
from .views import *

app_name = "capstoneapp"

urlpatterns = [
    path('businesses/', business_list, name='businesses'),
    path('business/form', business_form, name='business_form'),
    path('businesses/<int:business_id>/', business_details, name='business'),
    path('businesses/<int:business_id>/form/', business_edit_form, name='business_edit_form'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home'),
]