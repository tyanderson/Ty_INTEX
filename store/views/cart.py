__author__ = 'Charizard'

from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest
import homepage.models as hmod

templater = get_renderer('store')

@view_function
def process_request(request):
    template_vars = {}

    # If there is no shopping_cart session variable, make it!
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}

    # If item.id is already in shopping_cart, increment it by qty added, otherwise, set item.id as qty added
    if request.urlparams[0] in request.session['shopping_cart'].keys():
        request.session['shopping_cart'][request.urlparams[0]] = int(request.session['shopping_cart'][request.urlparams[0]]) + int(request.urlparams[1])
    else:
        # print(request.urlparams[0])
        request.session['shopping_cart'][request.urlparams[0]] = int(request.urlparams[1])

    # Save session variable changes
    request.session.modified = True

    # Get item
    try:
        # Get cart session dictionary keys
        keys = request.session['shopping_cart'].keys()
        # Grab only the items in the cart
        item = hmod.Sale_Product.objects.filter(id__in=keys)
        template_vars['item'] = item
    except hmod.Sale_Product.DoesNotExist:
        return HttpResponseRedirect('/store/index')

    return templater.render_to_response(request, 'cart.html', template_vars)

@view_function
def delete(request):
    template_vars = {}

    # Modify shopping_cart
    del request.session['shopping_cart'][str(request.urlparams[0])]

    # Save session variable changes
    request.session.modified = True

    # Get item
    try:
        # Get cart session dictionary keys
        keys = request.session['shopping_cart'].keys()
        # Grab only the items in the cart
        item = hmod.Sale_Product.objects.filter(id__in=keys)
        template_vars['item'] = item
    except hmod.Sale_Product.DoesNotExist:
        return HttpResponseRedirect('/store/index')

    return templater.render_to_response(request, 'cart.html', template_vars)

@view_function
def view(request):
    template_vars = {}
    # Get item
    if 'shopping_cart' in request.session:
        if len(request.session['shopping_cart']) > 0:
            try:
                # Get cart session dictionary keys
                keys = request.session['shopping_cart'].keys()
                # Grab only the items in the cart
                item = hmod.Sale_Product.objects.filter(id__in=keys)
                template_vars['item'] = item
            except hmod.Sale_Product.DoesNotExist:
                return templater.render_to_response(request, 'emptycart.html', template_vars)
            return templater.render_to_response(request, 'cart.html', template_vars)

    return templater.render_to_response(request, 'emptycart.html', template_vars)