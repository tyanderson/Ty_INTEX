from django.conf import settings
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
import homepage.models as hmod
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth import authenticate, login, logout
import time


templater = get_renderer('homepage')


############################################################
# Login
@view_function
def process_request(request):
    params = {}
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = hmod.User.objects.get(username=form.cleaned_data['username'])
                if user.is_active == False:
                    return HttpResponse('''
                        <script>
                            window.location.href = "/homepage/index/";
                        </script>
                    ''')
            except hmod.User.DoesNotExist:
                return HttpResponse('''
                        <script>
                            window.location.href = "/homepage/index/";
                        </script>
                    ''')
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return HttpResponse('''
                <script>
                    window.location.href = "/homepage/index/";
                </script>
            ''')

    params['form'] = form
    return templater.render_to_response(request, 'login.html', params)


############################################################
# Logout
@view_function
def logoutUser(request):
    logout(request)
    return templater.render_to_response(request, 'logoutUser.html')


############################################################
# Creates Login form
class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        min_length=0,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'true'})
    )
    password = forms.CharField(
        required=True,
        label='Password',
        min_length=0,
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean(self):
        user = authenticate(
            username=self.cleaned_data.get('username'),
            password=self.cleaned_data.get('password')
        )
        if user == None:
            raise forms.ValidationError('Username and password do not match.')
        return self.cleaned_data