import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from capstoneapp.models import Business, BusinessType, Customer
from .business_details import get_business


def get_business_types():
    return BusinessType.objects.all()


@login_required
def business_form(request):
    if request.method == 'GET':
        # """GETS a list of all business types to populate the dropdown in the add business form."""

        business_types = get_business_types()
        template = 'businesses/business_form.html'
        context = {
            'all_business_types': business_types
        }

        return render(request, template, context)


@login_required
def business_edit_form(request, business_id):

    if request.method == 'GET':

        # """GETS the details of a specific business to pre-fill the business edit form."""
        business = get_business(business_id)
        business_types = get_business_types
        template = 'businesses/business_form.html'
        context = {
            'business': business,
            'all_business_types': business_types
        }

        return render(request, template, context)
