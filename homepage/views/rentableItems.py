from django.conf import settings
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
import homepage.models as hmod
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
import time
from django.contrib.auth.decorators import permission_required


templater = get_renderer('homepage')


############################################################
# Shows the RentableItems
@view_function
@permission_required('homepage.add_rentableitem', '/homepage/accessDenied')
def process_request(request):
    params = {}
    try:
        # Gets all records in RentableItem table and assigns into params variable
        rentableItems = hmod.RentableItem.objects.all().order_by('id')
        params['rentableItems'] = rentableItems
    except hmod.RentableItem.DoesNotExist:
        # If it doesn't work, redirects back to homepage
        return HttpResponseRedirect('/homepage/index')

    # Renders the response to this page
    return templater.render_to_response(request, 'rentableItems.html', params)


############################################################
# Creates a RentableItem
@view_function
@permission_required('homepage.add_rentableitem', '/homepage/accessDenied')
def create(request):
    # Creates a new instance of a RentableItem
    newRentableItem = hmod.RentableItem()
    # Assigns values to rentable items
    newRentableItem.Name = ''
    newRentableItem.Description = ''
    newRentableItem.Value = 0
    newRentableItem.StandardRentalPrice = 0
    newRentableItem.LegalEntityID_id = 1
    newRentableItem.IsRentable = True
    newRentableItem.save()

    # After new user created, redirect to edit page, passing this new user id to be edited
    return HttpResponseRedirect('/homepage/rentableItems.edit/{}/'.format(newRentableItem.id))


############################################################
# Edits a single RentableItem
@view_function
@permission_required('homepage.change_rentableitem', '/homepage/accessDenied')
def edit(request):
    params = {}
    try:
        # Get user by id (id is taken from url parameter)
        rentableItem = hmod.RentableItem.objects.get(id=request.urlparams[0])
    except hmod.RentableItem.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentableItems')

    # Populate form based on user object attributes
    form = RentableItemEditForm(initial={
        'Name': rentableItem.Name,
        'Description': rentableItem.Description,
        'Value': rentableItem.Value,
        'StandardRentalPrice': rentableItem.StandardRentalPrice,
        #'LegalEntityID_id': rentableItem.LegalEntityID_id,
        #'IsRentable': rentableItem.IsRentable,
    })
    if request.method == 'POST':
        # Create form instance and populate it with the POST data
        form = RentableItemEditForm(request.POST)
        # If form is valid
        if form.is_valid():
            # make change on RentableItem object
            rentableItem.Name = form.cleaned_data['Name']
            rentableItem.Description = form.cleaned_data['Description']
            rentableItem.Value = form.cleaned_data['Value']
            rentableItem.StandardRentalPrice = form.cleaned_data['StandardRentalPrice']
            #rentableItem.IsRentable = form.cleaned_data['IsRentable']
            rentableItem.save()
            # Return to list of users
            return HttpResponseRedirect('/homepage/rentableItems')

    # If requested post is not valid, redirect back to users.edit page for corrections
    params['form'] = form
    params['rentableItem'] = rentableItem
    return templater.render_to_response(request, 'rentableItems.edit.html', params)


############################################################
# Deletes a single RentableItem
@view_function
@permission_required('homepage.delete_rentableitem', '/homepage/accessDenied')
def delete(request):
    try:
        rentableItem = hmod.RentableItem.objects.get(id=request.urlparams[0])
    except hmod.RentableItem.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentableItems')

    rentableItem.delete()
    return HttpResponseRedirect('/homepage/rentableItems')


############################################################
# Creates Edit form
class RentableItemEditForm(forms.Form):
    Name = forms.CharField(
        required=True,
        label='Name',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    Description = forms.CharField(
        required=True,
        label='Description',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    Value = forms.CharField(
        required=True,
        label='Value',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    StandardRentalPrice = forms.CharField(
        required=True,
        label='Standard Rental Price',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )