# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425524106.746791
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container-fluid" xmlns="http://www.w3.org/1999/html">\r\n        <div class="col-md-12 centerContent">\r\n            <div class="col-md-10 col-md-offset-1">\r\n\r\n')
        for field in form:
            __M_writer('                    <div class="col-sm-3"></div>\r\n                    <div class="col-sm-9">\r\n                        ')
            __M_writer(str(field.errors))
            __M_writer('\r\n                    </div>\r\n                    <div class="form-group">\r\n                        <label for=')
            __M_writer(str(field.name))
            __M_writer(' class="col-sm-3">')
            __M_writer(str(field.label))
            __M_writer('</label>\r\n                        <div class="col-sm-9">\r\n                            ')
            __M_writer(str(field))
            __M_writer('\r\n                        </div>\r\n                    </div>\r\n')
        __M_writer('\r\n            </div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "login.html", "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/login.html", "source_encoding": "ascii", "line_map": {"35": 1, "69": 63, "45": 3, "27": 0, "52": 3, "53": 8, "54": 9, "55": 11, "56": 11, "57": 14, "58": 14, "59": 14, "60": 14, "61": 16, "62": 16, "63": 20}}
__M_END_METADATA
"""
