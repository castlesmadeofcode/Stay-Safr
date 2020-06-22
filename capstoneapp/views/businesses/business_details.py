from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from capstoneapp.models import Business, Review
from django.contrib.auth.models import User


def get_business(business_id):
    return Business.objects.get(pk=business_id)


def business_details(request, business_id):
    if request.method == 'GET':
        business = get_business(business_id)
        all_reviews = Review.objects.filter(business_id=business_id)
        users = User.objects.all()

        template = 'businesses/business_detail.html'
        context = {
            'business': business,
            'all_reviews': all_reviews,
            'users': users
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting a business
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            business_to_delete = get_business(business_id)
            business_to_delete.delete()

            return redirect(reverse('capstoneapp:businesses'))

        # Check if this POST is for editing a business
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            business_to_update = get_business(business_id)

            business_to_update.name = form_data['name']
            business_to_update.price = form_data['price']
            business_to_update.description = form_data['description']
            business_to_update.location = form_data['location']
            business_to_update.phone_number = form_data['phone_number']
            business_to_update.address = form_data['address']
            business_to_update.website = form_data['website']
            business_to_update.business_type_id = form_data['business_type']

            business_to_update.save()

            # redirects back to the businesses details page after edit
            return redirect(reverse('capstoneapp:business', args=[business_to_update.id]))
