# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425772416.746322
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/cart.html'
_template_uri = 'cart.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        str = context.get('str', UNDEFINED)
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
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
        str = context.get('str', UNDEFINED)
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n\r\n    <!-- Loop through each request.session['shopping_cart'] -->\r\n\r\n")
        for i in item:
            __M_writer('        <div class="cart_item">\r\n            <div class="cart_item_data">\r\n                <img src="/static')
            __M_writer(str( i.photo ))
            __M_writer('" class="cart_thumbnail"/>\r\n            </div>\r\n            <div class="cart_item_data">\r\n                <p><b>Name: ')
            __M_writer(str(i.name))
            __M_writer('</b></p>\r\n                <p>Description: ')
            __M_writer(str(i.description))
            __M_writer('</p>\r\n                <p>Price: ')
            __M_writer(str( i.price ))
            __M_writer('</p>\r\n                <p>Quantity: ')
            __M_writer(str( request.session['shopping_cart'][str(i.id)] ))
            __M_writer('</p>\r\n                <p class="delete" data-item_id="')
            __M_writer(str(i.id))
            __M_writer('"><a href="#">Delete</a></p>\r\n            </div>\r\n        </div>\r\n        <hr>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 14, "65": 15, "66": 15, "27": 0, "68": 16, "37": 1, "70": 17, "71": 22, "77": 71, "47": 3, "67": 16, "69": 17, "56": 3, "57": 7, "58": 8, "59": 10, "60": 10, "61": 13, "62": 13, "63": 14}, "uri": "cart.html", "source_encoding": "ascii", "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/cart.html"}
__M_END_METADATA
"""
