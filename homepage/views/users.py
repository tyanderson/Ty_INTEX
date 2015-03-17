from django.conf import settings
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
import homepage.models as hmod
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
import time
from django.contrib.auth import logout
from django.contrib.auth.models import Group, Permission, ContentType
from django.contrib.auth.decorators import permission_required


templater = get_renderer('homepage')


############################################################
# Shows the Users
@view_function
@permission_required('homepage.add_user', '/homepage/accessDenied')
def process_request(request):
    params = {}
    try:
        # Gets all records in User table and assigns into params variable
        users = hmod.User.objects.filter(is_active=True).order_by('id')
        params['users'] = users
    except hmod.User.DoesNotExist:
        # If it doesn't work, redirects back to homepage
        return HttpResponseRedirect('/homepage/index/')

    # Renders the response to this page
    return templater.render_to_response(request, 'users.html', params)


############################################################
# Creates a User
@view_function
def create(request):
    # Delete any blank users
    try:
        user = hmod.User.objects.get(username='')
        user.delete()
    except hmod.User.DoesNotExist:
        pass

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
    newUser = hmod.User()
    # Assigns empty values to user
    newUser.set_password('')
    newUser.last_login = time.strftime('%Y-%m-%d %H:%M:%S')
    newUser.is_superuser = 0
    newUser.username = ''
    newUser.first_name = ''
    newUser.last_name = ''
    newUser.email = ''
    newUser.is_staff = 0
    newUser.is_active = 1
    newUser.date_joined = time.strftime('%Y-%m-%d %H:%M:%S')

    # Select max id from Address table
    try:
        address = hmod.Address.objects.all().order_by('-id')[0]
        # add(address_id)
        newUser.address_id = address.id
    except hmod.Address.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')

    # Saves instantiation and changes made
    newUser.save()



    # # Add new user to 'User' group
    # Select max id from User table
    try:
        user = hmod.User.objects.all().order_by('-id')[0]
        # add(group_id) group_id is 1 for user, 2 for manager, and 3 for admin
        newUser.groups.add(1)
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
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')

    # Fill form with object attributes
    form = UserEditForm(initial={
        'username': users.username,
        'first_name': users.first_name,
        'last_name': users.last_name,
        'email': users.email,
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
            return HttpResponseRedirect('/homepage/index')

    # If requested post is not valid, redirect back to users.edit page for corrections
    params['form'] = form
    params['users'] = users
    return templater.render_to_response(request, 'users.edit.html', params)


############################################################
# Archives a single User (sets is_active as false)
@view_function
def delete(request):
    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
        # Set account as innactive
        user.is_active = False
        user.save()
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')
    if request.urlparams[1] == "logout":
        logout(request)
    # Reload page
    return HttpResponseRedirect('/homepage/index')


############################################################
# Creates Edit form
class UserEditForm(forms.Form):
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

    def clean_username(self):
        users = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userID)
        if len(users) >= 1:
            raise forms.ValidationError('Username already taken. Please try another.')

        return self.cleaned_data['username']


############################################################
# Creates Edit form
class UserEditForm2(forms.Form):
    # Form fields
    username = forms.CharField(
        required=True,
        label='Username',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
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

    def clean_username(self):
        users = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userID)
        if len(users) >= 1:
            raise forms.ValidationError('Username already taken. Please try another.')

        return self.cleaned_data['username']


############################################################
# Edits a single User
@view_function
def edit2(request):
    params = {}
    try:
        # Get user by id (id is taken from url parameter)
        users = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')

    # Fill form with object attributes
    form = UserEditForm2(initial={
        'username': users.username,
        'first_name': users.first_name,
        'last_name': users.last_name,
        'email': users.email,
    })
    params['username'] = users.username
    # If page request is a POST
    if request.method == 'POST':
        # Fill form with POSTED attributes
        form = UserEditForm2(request.POST)
        form.userID = users.id
        # If form is valid
        if form.is_valid():
            users.username = form.cleaned_data['username']
            users.first_name = form.cleaned_data['first_name']
            users.last_name = form.cleaned_data['last_name']
            users.email = form.cleaned_data['email']
            users.save()
            # Return to list of users
            return HttpResponseRedirect('/homepage/index')

    # If requested post is not valid, redirect back to users.edit page for corrections
    params['form'] = form
    params['users'] = users
    return templater.render_to_response(request, 'users.edit.html', params)