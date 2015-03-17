__author__ = 'Charizard'

from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
import homepage.models as hmod

templater = get_renderer('store')

@view_function
def process_request(request):
    template_vars = {}
    try:
        template_vars['rentable_articles'] = hmod.Rentable_Article.objects.all().order_by('id')
    except hmod.Sale_Product.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    return templater.render_to_response(request, 'rentals.html', template_vars)