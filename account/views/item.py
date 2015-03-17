__author__ = 'Charizard'

from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
import homepage.models as hmod

templater = get_renderer('account')

@view_function
def process_request(request):
    template_vars = {}
    try:
        item = hmod.Sale_Product.objects.all().order_by('id')
        template_vars['catalog_items'] = item
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    # # Shopping cart
    # if "shopping_cart" not in request.session:
    #     request.session['shopping_cart'] = {}

    if "fn" not in request.session:
        request.session['fn'] = "FN"#django.contrib.auth.models.User.first_name
    #
    # if item.id in request.session['shopping_cart']:
    #     request.session['shopping_cart'][item.id] += 1
    # else:
    #     request.session['shopping_cart'][item.id] = 1

    return templater.render_to_response(request, 'indexBackup.html', template_vars)