__author__ = 'Charizard'

from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
import homepage.models as hmod

templater = get_renderer('store')

@view_function
def process_request(request):
    return templater.render_to_response(request, 'thankyou.html')