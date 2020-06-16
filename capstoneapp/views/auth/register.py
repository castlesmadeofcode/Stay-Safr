from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from capstoneapp.models import Customer, Business
from django.forms import ValidationError

# If you only have the Django auth User table in your database and you don't need additional data on registration, use the following tutorial:
#   https://overiq.com/django-1-10/django-creating-users-using-usercreationform/
# Here is another tutorail that shows a few different helpful implementations:
#   https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html
  
  
def register(request):
    if request.method == 'POST':
        form_data = request.POST
        
        try:
            if form_data['password'] != form_data['password_confirmation']:
                raise ValidationError("Password and password confirmation do not match.")
              
            new_user = User.objects.create_user(
                username=form_data['username'],
                password=form_data['password']
            )

            new_user.customer.address=form_data['address']
            new_user.customer.phone_number=form_data['phone_number']
            new_user.customer.image_path=form_data['image_path']
            new_user.customer.is_owner=False
            new_user.customer.save()
            
            user = authenticate(request, username=form_data['username'], password=form_data['password'])
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect(reverse('capstoneapp:home'))
        except Exception as e:
            messages.error(request, f'{type(e)}: {e}')
          
                
    businesses = Business.objects.all()
    template = 'registration/register.html'
    context = {
        'businesses': businesses
    }

    return render(request, template, context)