# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425794002.640895
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/account.html'
_template_uri = 'account.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['mainContent']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def mainContent():
            return render_mainContent(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainContent'):
            context['self'].mainContent(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def mainContent():
            return render_mainContent(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="col-md-12 centerContent">\r\n    <div class="col-md-8 col-md-offset-2">\r\n        <h1>Acount Information</h1>\r\n        <h4>Name: ')
        __M_writer(str(user.first_name))
        __M_writer(' ')
        __M_writer(str(user.last_name))
        __M_writer('</h4>\r\n        <h4>Username: ')
        __M_writer(str(user.username))
        __M_writer('</h4>\r\n        <h4>Email: ')
        __M_writer(str(user.email))
        __M_writer('</h4>\r\n        <p><a href="/changepassword">Change Password</a></p>\r\n        <p><a href="/users.edit2/')
        __M_writer(str(user.id))
        __M_writer('">Edit Account</a></p>\r\n        <p><a href="/users.delete/')
        __M_writer(str(user.id))
        __M_writer('/logout">Delete Account</a></p>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/account.html", "line_map": {"64": 12, "35": 1, "70": 64, "45": 3, "27": 0, "52": 3, "53": 7, "54": 7, "55": 7, "56": 7, "57": 8, "58": 8, "59": 9, "60": 9, "61": 11, "62": 11, "63": 12}, "uri": "account.html"}
__M_END_METADATA
"""
