from django.shortcuts import render, redirect, reverse
from capstoneapp.models import Business, Review
from django.contrib.auth.decorators import login_required
from .business_details import get_Avg
from django.db.models import Q


# def business_id(all_businesses):


def business_list(request):
    if request.method == 'GET':
        all_businesses = Business.objects.all()
        all_reviews = Review.objects.all()
        new_query = request.GET.get("q")
        if new_query:
            all_businesses = all_businesses.filter(name__icontains=new_query)

        for business in all_businesses:
            reviews = Review.objects.filter(business_id=business.id)
            get_avg = get_Avg(reviews)
            business.review_avg = get_avg
        sorted_businesses = sorted(
            all_businesses, key=lambda business: (business.review_avg), reverse=True)

        template = 'businesses/business_list.html'
        context = {
            'all_businesses': sorted_businesses,
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        form_files = request.FILES

        # creates a new instance of Business to add to the database using user input from form

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
