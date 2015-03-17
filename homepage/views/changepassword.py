from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')


@view_function
def process_request(request):
    template_params = {}
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return templater.render_to_response(request, '/account.html', template_params)

    template_params['form'] = form
    return templater.render_to_response(request, '/changepassword.html', template_params)