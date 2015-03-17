from django.conf import settings
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
import homepage.models as hmod
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
import time
from django.contrib.auth.models import Group, Permission, ContentType
from django.contrib.auth.decorators import permission_required


templater = get_renderer('homepage')


############################################################
# Shows the Users
@view_function
def process_request(request):
    # Creates a new instance of an address
    address = hmod.Address()
    # Assigns empty values to address
    address.address1 = ''
    address.city = ''
    address.state = ''
    address.zip_code = ''
    # Save new address
    address.save()

    # Creates a new instance of a User
    user = hmod.User()
    # Assigns empty values to user
    user.set_password('')
    user.last_login = time.strftime('%Y-%m-%d %H:%M:%S')
    user.is_superuser = 0
    user.username = ''
    user.first_name = ''
    user.last_name = ''
    user.email = ''
    user.is_staff = 0
    user.is_active = 1
    user.date_joined = time.strftime('%Y-%m-%d %H:%M:%S')
    # Saves instantiation and changes made
    user.save()

    # # Add new user and address to UserAddress table
    # Select max id from Address table
    try:
        address = hmod.Address.objects.order_by('-id')[0]
        # add(address_id)
        user.address.add(address)
    except hmod.Address.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')

    # # Add new user to 'User' group
    # Select max id from User table
    try:
        user = hmod.User.objects.order_by('-id')[0]
        # add(group_id) group_id is 1 for user, 2 for manager, and 3 for admin
        user.groups.add(1)
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')

    # After new user and address are created, redirect to edit page, passing this new user id to be edited
    return HttpResponseRedirect('/homepage/users.edit/{}/'.format(newUser.id))


############################################################
# Edits a single User
@view_function
def edit(request):
    params = {}
    try:
        # Get user by id (id is taken from url parameter)
        users = hmod.User.objects.get(id=request.urlparams[0])
        # # Get user's address
        #try:
        #    Get user's address_id from user_address table
        #    address_id = hmod.User.address.get(user_id=request.urlparams[0])
        #    Get address from hmod.Address
        #except hmod.User.DoesNotExist:
        #    return HttpResponseRedirect('/homepage/users/')
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    # Fill form with object attributes
    form = UserEditForm(initial={
        'password': users.password,
        'last_login': users.last_login,
        'is_superuser': users.is_superuser,
        'username': users.username,
        'first_name': users.first_name,
        'last_name': users.last_name,
        'email': users.email,
        'is_staff': users.is_staff,
        'is_active': users.is_active,
        'date_joined': users.date_joined,
    })
    params['username'] = users.username
    # If page request is a POST
    if request.method == 'POST':
        # Fill form with POSTED attributes
        form = UserEditForm(request.POST)
        form.userID = users.id
        # If form is valid
        if form.is_valid():
            # make change on User object
            users.set_password(form.cleaned_data['password'])
            # users.last_login = form.cleaned_data['last_login']
            # users.is_superuser = form.cleaned_data['is_superuser']
            users.username = form.cleaned_data['username']
            users.first_name = form.cleaned_data['first_name']
            users.last_name = form.cleaned_data['last_name']
            users.email = form.cleaned_data['email']

            # group.group_id = form.cleaned_data['group']

            # users.is_staff = form.cleaned_data['is_staff']
            # users.is_active = form.cleaned_data['is_active']
            # users.date_joined = form.cleaned_data['date_joined']
            users.save()
            # Return to list of users
            return HttpResponseRedirect('/homepage/users')

    # If requested post is not valid, redirect back to users.edit page for corrections
    params['form'] = form
    params['users'] = users
    return templater.render_to_response(request, 'users.edit.html', params)


############################################################
# Archives a single User (sets is_active as false)
@view_function
@permission_required('homepage.delete_user', '/homepage/accessDenied')
def delete(request):
    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
        # Set account as innactive
        user.is_active = False
        user.save()
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/users')
    # Reload page
    return HttpResponseRedirect('/homepage/users')


############################################################
# Creates Edit form
class UserEditForm(forms.Form):
    # Names for states
    ALASKA = 'AK'
    ALABAMA = 'AL'
    ARKANSAS = 'AR'
    ARIZONA = 'AZ'
    CALIFORNIA = 'CA'
    COLORADO = 'CO'
    CONNECTICUT = 'CT'
    DELAWARE = 'DE'
    FLORIDA = 'FL'
    GEORGIA = 'GA'
    HAWAII = 'HI'
    IOWA = 'IA'
    IDAHO = 'ID'
    ILLINOIS = 'IL'
    INDIANA = 'IN'
    KANSAS = 'KS'
    LOUISIANA = 'LA'
    MASSACHUSETTS = 'MA'
    MARYLAND = 'MD'
    MAINE = 'ME'
    MICHIGAN = 'MI'
    MINNESOTA = 'MN'
    MISSOURI = 'MO'
    MISSISSIPPI = 'MS'
    MONTANA = 'MT'
    NORTH_CAROLINA = 'NC'
    NORTH_DAKOTA = 'ND'
    NEBRASKA = 'NE'
    NEW_HAMPSHIRE = 'NH'
    NEW_JERSEY = 'NJ'
    NEW_MEXICO = 'NM'
    NEVADA = 'NV'
    NEW_YORK = 'NY'
    OHIO = 'OH'
    OKLAHOMA = 'OK'
    OREGON = 'OR'
    PENNSYLVANIA = 'PA'
    RHODE_ISLAND = 'RI'
    SOUTH_CAROLINA = 'SC'
    SOUTH_DAKOTA = 'SD'
    TENNESSEE = 'TN'
    TEXAS = 'TX'
    UTAH = 'UT'
    VIRGINIA = 'VA'
    VERMONT = 'VT'
    WASHINGTON = 'WA'
    WISCONSIN = 'WI'
    WEST_VIRGINIA = 'WV'
    WYOMING = 'WY'
    # Form fields
    username = forms.CharField(
        required=True,
        label='Username',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        required=True,
        label='Password',
        min_length=0,
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    # is_superuser
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
    email = forms.CharField(
        required=True,
        label='Email',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    # auth_group = forms.ModelChoiceField(
    #     queryset=Group.objects.all(),
    #     empty_label="",
    #     # Set option value
    #     to_field_name="id",
    #     label='Authorization Group',
    #     widget=forms.Select(attrs={'class': 'form-control'}),
    # )
    #
    #
    #
    #
    #
    # is_staff
    # is_active
    # date_joined
    # AddressID_id
    #
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
        label='ZIP',
        min_length=0,
        max_length=5,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.ChoiceField(
        label='State',
        choices=(
            (ALASKA, 'Alaska'),
            (ALABAMA, 'Alabama'),
            (ARKANSAS, 'Arkansas'),
            (ARIZONA, 'Arizona'),
            (CALIFORNIA, 'California'),
            (COLORADO, 'Colorado'),
            (CONNECTICUT, 'Connecticut'),
            (DELAWARE, 'Delaware'),
            (FLORIDA, 'Florida'),
            (GEORGIA, 'Georgia'),
            (HAWAII, 'Hawaii'),
            (IOWA, 'Iowa'),
            (IDAHO, 'Idaho'),
            (ILLINOIS, 'Illinois'),
            (INDIANA, 'Indiana'),
            (KANSAS, 'Kansas'),
            (LOUISIANA, 'Louisiana'),
            (MASSACHUSETTS, 'Massachusetts'),
            (MARYLAND, 'Maryland'),
            (MAINE, 'Maine'),
            (MICHIGAN, 'Michigan'),
            (MINNESOTA, 'Minnesota'),
            (MISSOURI, 'Missouri'),
            (MISSISSIPPI, 'Mississippi'),
            (MONTANA, 'Montana'),
            (NORTH_CAROLINA, 'North Carolina'),
            (NORTH_DAKOTA, 'North Dakota'),
            (NEBRASKA, 'Nebraska'),
            (NEW_HAMPSHIRE, 'New Hampshire'),
            (NEW_JERSEY, 'New Jersey'),
            (NEW_MEXICO, 'New Mexico'),
            (NEVADA, 'Nevada'),
            (NEW_YORK, 'New York'),
            (OHIO, 'Ohio'),
            (OKLAHOMA, 'Oklahoma'),
            (OREGON, 'Oregon'),
            (PENNSYLVANIA, 'Pennsylvania'),
            (RHODE_ISLAND, 'Rhode Island'),
            (SOUTH_CAROLINA, 'South Carolina'),
            (SOUTH_DAKOTA, 'South Dakota'),
            (TENNESSEE, 'Tennessee'),
            (TEXAS, 'Texas'),
            (UTAH, 'Utah'),
            (VIRGINIA, 'Virginia'),
            (VERMONT, 'Vermont'),
            (WASHINGTON, 'Washington'),
            (WISCONSIN, 'Wisconsin'),
            (WEST_VIRGINIA, 'West Virginia'),
            (WYOMING, 'Wyoming'),
        ),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean_username(self):
        users = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userID)
        if len(users) >= 1:
            raise forms.ValidationError('Username already taken. Please try another.')

        return self.cleaned_data['username']

