# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425795144.26468
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/batch.html'
_template_uri = 'batch.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        rentals = context.get('rentals', UNDEFINED)
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
        rentals = context.get('rentals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h1>Overdue Items:</h1>\r\n')
        for rental in rentals:
            __M_writer('        <h4>Name: ')
            __M_writer(str( rental.rentable_article.name ))
            __M_writer('</h4>\r\n        <p style="padding-left: 20px;">Value: $')
            __M_writer(str( rental.rentable_article.value ))
            __M_writer('</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "batch.html", "line_map": {"64": 58, "35": 1, "52": 3, "53": 5, "54": 6, "55": 6, "56": 6, "57": 7, "58": 7, "27": 0, "45": 3}, "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/batch.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
