# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425786404.534276
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/changepassword.html'
_template_uri = '/changepassword.html'
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
        form = context.get('form', UNDEFINED)
        def mainContent():
            return render_mainContent(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        def mainContent():
            return render_mainContent(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="col-md-12 centerContent">\r\n    <div class="col-md-6 col-md-offset-3">\r\n        <h1>Change Password</h1>\r\n        <form method="POST" class="form-horizontal">\r\n\r\n')
        for field in form:
            __M_writer('                <div class="form-group">\r\n                    <div class="col-sm-3"></div>\r\n                    <div class="col-sm-9">')
            __M_writer(str(field.errors))
            __M_writer('</div>\r\n                    <label for=')
            __M_writer(str(field.name))
            __M_writer(' class="col-sm-3">')
            __M_writer(str(field.label))
            __M_writer('</label>\r\n                    <div class="col-sm-9">\r\n                        ')
            __M_writer(str(field))
            __M_writer('\r\n                    </div>\r\n                </div>\r\n')
        __M_writer('\r\n            <a class="btn btn-default" href="')
        __M_writer(str(request.META['HTTP_REFERER']))
        __M_writer('" role="button">Back</a>\r\n            <button type="submit" class="btn btn-primary col-sm-offset-9">Submit</button>\r\n        </form>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/changepassword.html", "source_encoding": "ascii", "uri": "/changepassword.html", "line_map": {"64": 15, "65": 19, "66": 20, "27": 0, "36": 1, "73": 67, "46": 3, "67": 20, "54": 3, "55": 9, "56": 10, "57": 12, "58": 12, "59": 13, "60": 13, "61": 13, "62": 13, "63": 15}}
__M_END_METADATA
"""
