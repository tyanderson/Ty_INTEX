from django.conf import settings
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
import homepage.models as hmod
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
import datetime
from django.contrib.auth.decorators import permission_required


templater = get_renderer('homepage')


############################################################
# Shows the Areas
@view_function
@permission_required('homepage.add_area', '/homepage/accessDenied')
def process_request(request):
    params = {}
    try:
        areas = hmod.Area.objects.all().order_by('id')
        params['areas'] = areas
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    return templater.render_to_response(request, 'areas.html', params)


############################################################
# Creates a single Area
@view_function
@permission_required('homepage.add_area', '/homepage/accessDenied')
def createArea(request):
    # Creates a new instance of an Area
    area = hmod.Area()
    # Assigns empty values to Event
    area.Name = ''
    area.Description = ''
    area.PlaceNumber = ''
    area.Event_id = 1
    # Saves instantiation and changes made
    area.save()

    # After new Area is created, redirect to edit page, passing this new Area id to be edited
    return HttpResponseRedirect('/homepage/areas.editArea/{}'.format(area.id))


############################################################
# Edits a single Event
@view_function
@permission_required('homepage.change_area', '/homepage/accessDenied')
def editArea(request):
    params = {}
    try:
        areas = hmod.Area.objects.get(id=request.urlparams[0])
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/areas')

    form = AreaEditForm(initial={
        'Name': areas.Name,
        'Description': areas.Description,
        'PlaceNumber': areas.PlaceNumber,
    })
    # If the SUBMIT button was pressed (meaning there was a POST form called)
    if request.method == 'POST':
        form = AreaEditForm(request.POST)
        if form.is_valid():
            # make change on Event object
            areas.Name = form.cleaned_data['Name']
            areas.Description= form.cleaned_data['Description']
            areas.PlaceNumber = form.cleaned_data['PlaceNumber']
            # Save changes
            areas.save()
            return HttpResponseRedirect('/homepage/areas')

    params['form'] = form
    return templater.render_to_response(request, 'areas.editArea.html', params)


class AreaEditForm(forms.Form):
    Name = forms.CharField(
        required=True,
        min_length=0,
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    Description = forms.CharField(
        required=True,
        min_length=0,
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    PlaceNumber = forms.CharField(
        required=True,
        min_length=0,
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


############################################################
# Deletes a single Area
@view_function
@permission_required('homepage.delete_area', '/homepage/accessDenied')
def deleteArea(request):
    try:
        area = hmod.Area.objects.get(id=request.urlparams[0])
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/areas/')

    area.delete()
    return HttpResponseRedirect('/homepage/areas/')