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
# Shows the Events
@view_function
@permission_required('homepage.add_event', '/homepage/accessDenied')
def process_request(request):
    params = {}
    # Get events
    try:
        # Get events
        events = hmod.Event.objects.all().order_by('id')
        # Pass objects to parameters variable
        params['events'] = events
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    return templater.render_to_response(request, 'events.html', params)


############################################################
# Creates a single Event
@view_function
@permission_required('homepage.add_event', '/homepage/accessDenied')
def create(request):
    # Creates a new instance of an Event
    event = hmod.Event()
    # Assigns empty values to Event
    event.StartDate = '2015-01-01'
    event.EndDate = '2015-01-01'
    event.MapFileName = ''
    # Saves instantiation and changes made
    event.save()

    # After new Event is created, redirect to edit page, passing this new Event id to be edited
    return HttpResponseRedirect('/homepage/events.edit/{}'.format(event.id))


############################################################
# Edits a single Event
@view_function
@permission_required('homepage.change_event', '/homepage/accessDenied')
def edit(request):
    params = {}
    try:
        # Get events
        events = hmod.Event.objects.get(id=request.urlparams[0])
        # Get areas
        areas = hmod.Area.objects.all().filter(EventID_id=request.urlparams[0]).order_by('id')
        # Get venues
        venues = hmod.Venue.objects.all().filter(EventID_id=request.urlparams[0]).order_by('id')
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events')

    form = EventEditForm(initial={
        'StartDate': events.StartDate,
        'EndDate': events.EndDate,
        'MapFileName': events.MapFileName,
    })
    # If the SUBMIT button was pressed (meaning there was a POST form called)
    if request.method == 'POST':
        form = EventEditForm(request.POST)
        if form.is_valid():
            # make change on Event object
            events.StartDate = form.cleaned_data['StartDate']
            events.EndDate = form.cleaned_data['EndDate']
            events.MapFileName = form.cleaned_data['MapFileName']
            # Save changes
            events.save()
            return HttpResponseRedirect('/homepage/events')

    params['form'] = form
    params['areas'] = areas
    params['venues'] = venues
    return templater.render_to_response(request, 'events.edit.html', params)


class EventEditForm(forms.Form):
    StartDate = forms.DateField(
        #initial=datetime.date.today,
        label='Start Date',
        widget=forms.DateInput(attrs={'class': 'form-control'})
    )
    EndDate = forms.DateField(
        #initial=datetime.date.today,
        label='End Date',
        widget=forms.DateInput(attrs={'class': 'form-control'})
    )
    # Area = forms.ModelChoiceField(
    #     queryset=hmod.Area.objects.all(),
    #     empty_label="",
    #     # Set option value
    #     to_field_name="id",
    #     label='Area',
    #     widget=forms.Select(attrs={'class': 'form-control'}),
    # )
    MapFileName = forms.CharField(
        required=True,
        label='Map File Name',
        min_length=0,
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


############################################################
# Deletes a single Event
@view_function
@permission_required('homepage.delete_event', '/homepage/accessDenied')
def delete(request):
    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')

    event.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


########################################################################################################################
#                                                           AREAS                                                      #
########################################################################################################################
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
    # Get end digits from referer page
    EventID = request.META['HTTP_REFERER'].split("events.edit/", 1)[1]
    area.EventID_id = EventID
    # Saves instantiation and changes made
    area.save()

    # After new Area is created, redirect to edit page, passing this new Area id to be edited
    return HttpResponseRedirect('/homepage/events.editArea/{}'.format(area.id))


############################################################
# Edits a single Event
@view_function
@permission_required('homepage.change_area', '/homepage/accessDenied')
def editArea(request):
    params = {}
    try:
        areas = hmod.Area.objects.get(id=request.urlparams[0])
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/events')

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
            areas.Description = form.cleaned_data['Description']
            areas.PlaceNumber = form.cleaned_data['PlaceNumber']
            # Save changes
            areas.save()
            return HttpResponseRedirect('/homepage/events.edit/' + str(areas.EventID_id))

    params['form'] = form
    params['eventID'] = request.urlparams[0]
    return templater.render_to_response(request, 'events.editArea.html', params)


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
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


########################################################################################################################
#                                                           Venues                                                     #
########################################################################################################################
############################################################
# Creates a single venue
@view_function
@permission_required('homepage.add_venue', '/homepage/accessDenied')
def createVenue(request):
    # Creates a new instance of a venue
    venue = hmod.Venue()
    # Assigns empty values to venue
    venue.Name = ''
    # Get end digits from referer page
    EventID = request.META['HTTP_REFERER'].split("events.edit/", 1)[1]
    venue.EventID_id = EventID
    # Saves instantiation and changes made
    venue.save()

    # After new venue is created, redirect to edit page, passing this new venue id to be edited
    return HttpResponseRedirect('/homepage/events.editVenue/{}'.format(venue.id))


############################################################
# Edits a single venue
@view_function
@permission_required('homepage.change_venue', '/homepage/accessDenied')
def editVenue(request):
    params = {}
    try:
        venues = hmod.Venue.objects.get(id=request.urlparams[0])
    except hmod.Venue.DoesNotExist:
        return HttpResponseRedirect('/homepage/events')

    form = VenueEditForm(initial={
        'Name': venues.Name,
    })
    # If the SUBMIT button was pressed (meaning there was a POST form called)
    if request.method == 'POST':
        form = VenueEditForm(request.POST)
        if form.is_valid():
            # make change on venue object
            venues.Name = form.cleaned_data['Name']
            # Save changes
            venues.save()
            return HttpResponseRedirect('/homepage/events.edit/' + str(venues.EventID_id))

    params['form'] = form
    params['eventID'] = request.urlparams[0]
    return templater.render_to_response(request, 'events.editArea.html', params)


class VenueEditForm(forms.Form):
    Name = forms.CharField(
        required=True,
        min_length=0,
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


############################################################
# Deletes a single Area
@view_function
@permission_required('homepage.delete_venue', '/homepage/accessDenied')
def deleteVenue(request):
    try:
        venue = hmod.Venue.objects.get(id=request.urlparams[0])
    except hmod.Venue.DoesNotExist:
        return HttpResponseRedirect('/homepage/events')

    venue.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])