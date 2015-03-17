from django.http import HttpResponseRedirect

__author__ = 'Charizard'

from django_mako_plus.controller import view_function
from django import forms
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import datetime

templater = get_renderer('store')


@view_function
def process_request(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            return HttpResponseRedirect('/store/thankyou')
        template_params = {}
        template_params['form'] = checkoutForm()
        return templater.render_to_response(request, '/checkout.html', template_params)
    else:
        return templater.render_to_response(request, '/homepage/templates/accessDenied.html')


############################################################
# Creates Edit form
class checkoutForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        label='First Name',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address1 = forms.CharField(
        required=True,
        label='Address 1',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address2 = forms.CharField(
        required=False,
        label='Address 2',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    city = forms.CharField(
        required=True,
        label='City',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    zip = forms.CharField(
        required=True,
        label='Zip',
        min_length=0,
        max_length=5,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    credit_card = forms.CharField(
        required=True,
        label='Credit Card',
        min_length=16,
        max_length=16,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    security_code = forms.CharField(
        required=True,
        label='Security Code',
        min_length=3,
        max_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    exp_day = forms.ChoiceField(
        required=True,
        label='Exp Day',
        choices=(
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10'),
            (11, '11'),
            (12, '12'),
            (13, '13'),
            (14, '14'),
            (15, '15'),
            (16, '16'),
            (17, '17'),
            (18, '18'),
            (19, '19'),
            (20, '20'),
            (21, '21'),
            (22, '22'),
            (23, '23'),
            (24, '24'),
            (25, '25'),
            (26, '26'),
            (27, '27'),
            (28, '28'),
            (29, '29'),
            (30, '30'),
            (31, '31'),
        ),
        widget=forms.Select(attrs={'class': 'form-control exp_date'})
    )
    exp_month = forms.ChoiceField(
        required=True,
        label='Exp Month',
        choices=(
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10'),
            (11, '11'),
            (12, '12'),
        ),
        widget=forms.Select(attrs={'class': 'form-control exp_date'})
    )
    exp_year = forms.ChoiceField(
        required=True,
        label='Exp Year',
        choices=(
            (15, '15'),
            (16, '16'),
            (17, '17'),
            (18, '18'),
            (19, '19'),
            (20, '20'),
            (21, '21'),
            (22, '22'),
            (23, '23'),
            (24, '24'),
            (25, '25'),
            (26, '26'),
            (27, '27'),
            (28, '28'),
            (29, '29'),
            (30, '30'),
        ),
        widget=forms.Select(attrs={'class': 'form-control exp_date'})
    )