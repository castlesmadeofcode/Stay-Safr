from django.shortcuts import render, redirect, reverse
from capstoneapp.models import Business, Review
from django.contrib.auth.decorators import login_required
from .business_details import get_Avg
from django.db.models import Q


# def business_id(all_businesses):
#     for business in all_businesses:
#         print(business.id)
#         return business.id


def business_list(request):
    if request.method == 'GET':
        all_businesses = Business.objects.all()
        new_query = Business.objects.filter(name__icontains='new')
        # new_bus = business_id(all_businesses)
        # all_reviews = Review.objects.filter(
        # business_id=new_bus)
        # theAvg = get_Avg(all_reviews)

        template = 'businesses/business_list.html'
        context = {
            'all_businesses': all_businesses,
            # 'theAvg': theAvg
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        form_files = request.FILES

        new_business = Business.objects.create(
            name=form_data['name'],
            price=form_data['price'],
            description=form_data['description'],
            customer_id=request.user.customer.id,
            location=form_data['location'],
            phone_number=form_data['phone_number'],
            address=form_data['address'],
            website=form_data['website'],
            image=form_files['image'],
            business_type_id=form_data['business_type'],
        )

        return redirect(reverse('capstoneapp:businesses'))
