from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from capstoneapp.models import Review


def get_review(review_id):
    return Review.objects.get(pk=review_id)


@login_required
def review_details(request, review_id):

    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting a review
        #
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):

            # """Makes a POST request to delete a review and then re-directs to the business detail page."""

            review_to_delete = get_review(review_id)
            review_to_delete.delete()

            return redirect(reverse('capstoneapp:business', args=[review_to_delete.business_id]))

        # Check if this POST is for editing a review
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

           # """Makes a POST request to update an existing review and then re-directs to the business detail page."""

            review_to_update = get_review(review_id)
            review_to_update.rating = form_data['rating']
            review_to_update.comment = form_data['comment']
            review_to_update.save()

            return redirect(reverse('capstoneapp:business', args=[review_to_update.business_id]))
