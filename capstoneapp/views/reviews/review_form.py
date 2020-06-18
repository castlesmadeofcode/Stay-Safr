import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from capstoneapp.models import Review, Business
from .review_details import get_review




# def get_business():
#     return Business.objects.all()


@login_required
def review_form(request):
    if request.method == 'GET':
        # business = get_business()
        template = 'reviews/review_form.html'
        context = {
            # 'all_business': business
        }

        return render(request, template, context)

@login_required
def review_edit_form(request, review_id):

    if request.method == 'GET':
        review = get_review(review_id)
        # business = get_business
        template = 'reviews/review_form.html'
        context = {
            'review': review,
            # 'all_business': business
        }


        return render(request, template, context)