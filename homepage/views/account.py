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
# Shows the User data
@view_function
def process_request(request):
    params = {}
    if request.user.is_authenticated():
        try:
            user = hmod.User.objects.get(id=request.user.id)
            params['user'] = user
            return templater.render_to_response(request, 'account.html', params)
        except hmod.User.DoesNotExist:
            return HttpResponseRedirect('/homepage/index')

    return templater.render_to_response(request, 'index.html', params)