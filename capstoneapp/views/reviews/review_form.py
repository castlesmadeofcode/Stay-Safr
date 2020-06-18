import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from capstoneapp.models import Review, Business
from .review_details import get_review



@login_required
def review_form(request):
    if request.method == 'GET':
        business_id = request.GET['business_id']
        print(business_id)
        template = 'reviews/review_form.html'
        context = {
            'business_id': business_id
        }

        return render(request, template, context)

@login_required
def review_edit_form(request, review_id):

    if request.method == 'GET':
        review = get_review(review_id)
        business_id = request.GET['business_id']
        template = 'reviews/review_form.html'
        context = {
            'review': review,
            'business_id': business_id
        }


        return render(request, template, context)