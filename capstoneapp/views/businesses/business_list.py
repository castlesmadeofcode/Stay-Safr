from django.shortcuts import render, redirect, reverse
from capstoneapp.models import Business, Review
from django.contrib.auth.decorators import login_required
from .business_details import get_Avg
from django.db.models import Q


def business_list(request):
    if request.method == 'GET':

        # """GETS all of the business and review objects."""

        all_businesses = Business.objects.all()
        all_reviews = Review.objects.all()
        new_query = request.GET.get("q")
        if new_query:
            all_businesses = all_businesses.filter(name__icontains=new_query)

        # """GETS all of the reviews associated with a business, calculates the average rating of reviews, sorts businesses based on average rating from high to low ."""

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


        # """Makes a POST request to add a new business and then re-directs to the business list page."""
        # creates a new instance of Business to add to the database using user input from form

        new_business = Business.objects.create(
            name=form_data['name'],
            description=form_data['description'],
            customer_id=request.user.customer.id,
            phone_number=form_data['phone_number'],
            address=form_data['address'],
            website=form_data['website'],
            image=form_files['image'],
            business_type_id=form_data['business_type'],
        )

        return redirect(reverse('capstoneapp:businesses'))
