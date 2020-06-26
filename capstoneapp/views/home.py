from django.shortcuts import render
from capstoneapp.models import Business, Review
from .businesses.business_details import get_Avg


def home(request):
    if request.method == 'GET':
        all_businesses = Business.objects.all()

    if request.method == 'GET':
        all_businesses = Business.objects.all()
        all_reviews = Review.objects.all()

        for business in all_businesses:
            reviews = Review.objects.filter(business_id=business.id)
            get_avg = get_Avg(reviews)
            business.review_avg = get_avg
        sorted_businesses = sorted(
            all_businesses, key=lambda business: (business.review_avg), reverse=True)
        print(sorted_businesses)

        template = 'home.html'
        context = {
            'all_businesses': sorted_businesses,
        }

        return render(request, template, context)
