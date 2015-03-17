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
from homepage.views.login import LoginForm


templater = get_renderer('homepage')


@view_function
def process_request(request):
    template_vars = {}
    try:
        rentals = hmod.Rental_Item.objects.filter(
            date_due__lt=datetime.datetime.today(),
            return_set__iexact=None
        )
    except hmod.Rental_Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    template_vars['rentals'] = rentals
    return templater.render_to_response(request, 'batch.html', template_vars)