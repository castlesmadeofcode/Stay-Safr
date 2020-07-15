from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from capstoneapp.models import Business, Review
from django.contrib.auth.models import User


def get_business(business_id):
    return Business.objects.get(pk=business_id)

    # if a business has a review, find the average of all reviews associated with that business


def get_Avg(all_reviews):
    theSum = 0
    if len(all_reviews) != 0:
        for review in all_reviews:
            if review is not None:
                theSum += review.rating
                newAvg = theSum/len(all_reviews)
        return str(round(newAvg))
    else:
        return '0'


def business_details(request, business_id):
    if request.method == 'GET':

        # """GETS all of the reviews associated with a business, calculates the average rating of reviews, sorts businesses based on average rating from high to low ."""

        business = get_business(business_id)
        all_reviews = Review.objects.filter(business_id=business_id)
        users = User.objects.all()
        theAvg = get_Avg(all_reviews)
        submitted = False
        if request.user.is_authenticated:

            #    if the review.customer_id matches the logged in user id and review.business_id = business_id and both are greater than 0
            # submitted is set to True (submitted is originally set to false, upon becming true the add review button will not show)

            if len(Review.objects.filter(customer_id=request.user.customer.id, business_id=business_id)) > 0:
                submitted = True

        template = 'businesses/business_detail.html'
        context = {
            'business': business,
            'all_reviews': all_reviews,
            'users': users,
            'theAvg': theAvg,
            'submitted': submitted

        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting a business

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):

            # """Makes a POST request to delete a business and then re-directs to the business list page."""

            business_to_delete = get_business(business_id)
            business_to_delete.delete()

            return redirect(reverse('capstoneapp:businesses'))

        # Check if this POST is for editing a business
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            # """Makes a POST request to update an existing business and then re-directs to the business detail page."""

            business_to_update = get_business(business_id)

            business_to_update.name = form_data['name']
            business_to_update.description = form_data['description']
            business_to_update.phone_number = form_data['phone_number']
            business_to_update.address = form_data['address']
            business_to_update.website = form_data['website']
            business_to_update.business_type_id = form_data['business_type']

            business_to_update.save()

            # redirects back to the businesses details page after edit
            return redirect(reverse('capstoneapp:business', args=[business_to_update.id]))
