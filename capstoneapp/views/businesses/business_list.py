from django.shortcuts import render, redirect, reverse
from capstoneapp.models import Business
from django.contrib.auth.decorators import login_required



def business_list(request):
    if request.method == 'GET':
        all_businesses = Business.objects.all()

        template = 'businesses/business_list.html'
        context = {
            'all_businesses': all_businesses
        }

        return render(request, template, context)
      
    elif request.method == 'POST':
        form_data = request.POST
        form_files = request.FILES

        
    
        
        new_business = Business.objects.create(
            name = form_data['name'],
            price = form_data['price'],
            description = form_data['description'],
            customer_id = request.user.customer.id,
            location = form_data['location'],
            phone_number = form_data['phone_number'],
            address = form_data['address'],
            website = form_data['website'],
            image = form_files['image'],
            business_type_id = form_data['business_type'],
        )
        

        return redirect(reverse('capstoneapp:businesses'))