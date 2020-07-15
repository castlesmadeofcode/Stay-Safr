from django.shortcuts import render, redirect, reverse
from capstoneapp.models import Review
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required
def create_review(request):

    if request.method == 'POST':
        form_data = request.POST

    # """Makes a POST request to add a new review and then re-directs to the review detail page."""

        new_review = Review.objects.create(
            rating=form_data['rating'],
            comment=form_data['comment'],
            created_at=datetime.now(),
            customer_id=request.user.customer.id,
            business_id=form_data['business_id'],
        )

    return redirect(reverse('capstoneapp:business', args=[new_review.business_id]))
