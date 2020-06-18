from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from capstoneapp.models import Review


def get_review(review_id):
    return Review.objects.get(pk=review_id)


@login_required
def review_details(request, review_id):
    if request.method == 'GET':
        review = get_review(review_id)

        template = 'reviews/review_detail.html'
        context = {
            'review': review
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting a review
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            review_to_delete = get_review(review_id)
            review_to_delete.delete()

            return redirect(reverse('capstoneapp:reviews'))

        # Check if this POST is for editing a review
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            review_to_update = get_review(review_id)
            review_to_update.rating = form_data['rating']
            review_to_update.comment = form_data['comment']
            review_to_update.save()

            #redirects back to the reviews details page after edit
            return redirect(reverse('capstoneapp:review', args=[review_to_update.id]))