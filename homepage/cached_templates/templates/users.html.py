# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425423704.640388
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/users.html'
_template_uri = 'users.html'
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
        users = context.get('users', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="col-md-12 centerContent">\r\n    <div class="col-md-10 col-md-offset-1">\r\n        <h1 class="inline">\r\n            Users\r\n        </h1>\r\n        <a href="/homepage/users.create" class="topViewLinks">\r\n            <span class="glyphicon glyphiconSmall glyphicon-plus-sign" aria-hidden="true"></span>\r\n            Add\r\n        </a>\r\n        <div class="tableBG">\r\n            <table class="table table-striped table-hover">\r\n                <tr>\r\n                    <th>ID</th>\r\n                    <th>First Name</th>\r\n                    <th>Last Name</th>\r\n                    <th>Username</th>\r\n                    <th>User Type</th>\r\n                </tr>\r\n')
        if users.__len__()>0:
            for user in users:
                __M_writer('                        <tr>\r\n                            <td>')
                __M_writer(str(user.id))
                __M_writer('</td>\r\n                            <td>')
                __M_writer(str(user.first_name))
                __M_writer('</td>\r\n                            <td>')
                __M_writer(str(user.last_name))
                __M_writer('</td>\r\n                            <td>')
                __M_writer(str(user.username))
                __M_writer('</td>\r\n                            <td>\r\n                                ...\r\n                                <div class="inline">\r\n                                    <a href="/homepage/users.edit/')
                __M_writer(str(user.id))
                __M_writer('">\r\n                                        <span class="glyphicon glyphiconSmall glyphicon-pencil" aria-hidden="true"></span>\r\n                                    </a>\r\n                                    <a href="/homepage/users.delete/')
                __M_writer(str(user.id))
                __M_writer('">\r\n                                        <span class="glyphicon glyphiconSmall glyphicon-trash" aria-hidden="true"></span>\r\n                                    </a>\r\n                                </div>\r\n                            </td>\r\n                        </tr>\r\n')
        else:
            __M_writer('                    <tr>\r\n                        <td></td>\r\n                        <td></td>\r\n                        <td></td>\r\n                        <td></td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n        </div>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "users.html", "line_map": {"64": 32, "65": 32, "66": 35, "67": 35, "68": 42, "69": 43, "70": 50, "76": 70, "27": 0, "35": 1, "45": 3, "52": 3, "53": 22, "54": 23, "55": 24, "56": 25, "57": 25, "58": 26, "59": 26, "60": 27, "61": 27, "62": 28, "63": 28}, "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/users.html"}
__M_END_METADATA
"""
