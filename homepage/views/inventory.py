from django.conf import settings
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
import homepage.models as hmod
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required


templater = get_renderer('homepage')


############################################################
# Shows the SaleItems
@view_function
@permission_required('homepage.add_saleitem', '/homepage/accessDenied')
def process_request(request):
    params = {}
    try:
        saleitem = hmod.SaleItem.objects.all().order_by('id')
        params['saleitem'] = saleitem
    except hmod.SaleItem.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    return templater.render_to_response(request, 'inventory.html', params)


############################################################
# Creates a SaleItem
@view_function
@permission_required('homepage.add_saleitem', '/homepage/accessDenied')
def create(request):
    # Creates a new instance of a SaleItem
    item = hmod.SaleItem()
    # Assigns empty values to SaleItem
    item.Name = ''
    item.Description = ''
    item.LowPrice = '0.00'
    item.HighPrice = '0.00'
    #item.AreaID_id = ''
    # Saves instantiation and changes made
    item.save()

    # After new SaleItem is created, redirect to edit page, passing this new SaleItem id to be edited
    return HttpResponseRedirect('/homepage/inventory.edit/{}'.format(item.id))


############################################################
# Edits a single SaleItem
@view_function
@permission_required('homepage.change_saleitem', '/homepage/accessDenied')
def edit(request):
    params = {}
    try:
        saleitem = hmod.SaleItem.objects.get(id=request.urlparams[0])
    except hmod.SaleItem.DoesNotExist:
        return HttpResponseRedirect('/homepage/inventory')

    form = SaleItemEditForm(initial={
        'name': saleitem.Name,
        'description': saleitem.Description,
        'highPrice': saleitem.HighPrice,
        'lowPrice': saleitem.LowPrice,
        'area': saleitem.AreaID_id,
    })
    if request.method == 'POST':
        form = SaleItemEditForm(request.POST)
        if form.is_valid():
            # make change on SaleItem object
            saleitem.Name = form.cleaned_data['name']
            saleitem.Description = form.cleaned_data['description']
            saleitem.LowPrice = form.cleaned_data['lowPrice']
            saleitem.HighPrice = form.cleaned_data['highPrice']
            saleitem.AreaID_id = form.cleaned_data['area']
            saleitem.save()
            return HttpResponseRedirect('/homepage/inventory')

    params['form'] = form
    return templater.render_to_response(request, 'inventory.edit.html', params)


############################################################
# Deletes a single SaleItem
@view_function
@permission_required('homepage.delete_saleitem', '/homepage/accessDenied')
def delete(request):
    try:
        saleitem = hmod.SaleItem.objects.get(id=request.urlparams[0])
    except hmod.SaleItem.DoesNotExist:
        return HttpResponseRedirect('/homepage/inventory')

    saleitem.delete()
    return HttpResponseRedirect('/homepage/inventory')


############################################################
# Creates Edit form
class SaleItemEditForm(forms.Form):
    name = forms.CharField(
        required=True,
        label='Item Name',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        required=True,
        label='Description',
        min_length=0,
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    lowPrice = forms.DecimalField(
        required=True,
        label='Low Price',
        decimal_places=2,
        max_digits=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    highPrice = forms.DecimalField(
        required=True,
        label='High Price',
        decimal_places=2,
        max_digits=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    area = forms.ModelChoiceField(
        queryset=hmod.Area.objects.all(),
        empty_label="",
        # Set option value
        to_field_name="id",
        label='Area',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )