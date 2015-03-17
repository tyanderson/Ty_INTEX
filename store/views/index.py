__author__ = 'Charizard'

from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
import homepage.models as hmod

templater = get_renderer('store')

@view_function
def process_request(request):
    print("4444444444444444444444444444")
    if request.urlparams[0]:
        return templater.render_to_response(request, 'item.html')
    template_vars = {}
    try:
        item = hmod.Sale_Product.objects.all().order_by('id')
        template_vars['catalog_items'] = item
    except hmod.Sale_Product.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    return templater.render_to_response(request, 'index.html', template_vars)


############################################################
# Views a specific item
@view_function
def itemview(request):
    template_vars = {}
    try:
        template_vars['item'] = hmod.Sale_Product.objects.get(id=request.urlparams[0])
        try:
            template_vars['photo'] = hmod.Photograph.objects.get(id=template_vars['item'].photo_id)
        except hmod.Photograph.DoesNotExist:
            return HttpResponseRedirect('/homepage/index')
    except hmod.Sale_Product.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    return templater.render_to_response(request, 'index.itemview.html', template_vars)


############################################################
# Views a specific item
@view_function
def search(request):
    template_vars = {}
    try:
        items = hmod.Sale_Product.objects.all().filter(name__icontains=request.urlparams[0])
        template_vars['catalog_items'] = items
    except hmod.Sale_Product.DoesNotExist:
        return templater.render_to_response(request, 'noitems.html', template_vars)
    return templater.render_to_response(request, 'indexitems.html', template_vars)