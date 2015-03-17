# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426198173.614167
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/index.html'
_template_uri = 'index.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        catalog_items = context.get('catalog_items', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        catalog_items = context.get('catalog_items', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="col-md-3" id="left_col">\r\n        ')
        runtime._include_file(context, '/store/templates/left_col.html', _template_uri)
        __M_writer('\r\n    </div>\r\n    <div class="col-md-9" id="items">\r\n        <div class="col-md-11" id="search_bar">\r\n            <ul class="nav navbar-nav navbar-right" id="navbar-right">\r\n                <form class="navbar-form navbar-left" role="search">\r\n                    <div class="form-group">\r\n                        <input type="text" id="search_input" class="form-control" placeholder="Search the store">\r\n                    </div>\r\n                    <button type="button" id="search_button" class="btn btn-primary">Search</button>\r\n                </form>\r\n            </ul>\r\n        </div>\r\n')
        for item in catalog_items:
            __M_writer('            <div class="col-md-3 item_display">\r\n                <a href="/store/index.itemview/')
            __M_writer(str(item.id))
            __M_writer('">\r\n                    <img class="item_photo" src="/static')
            __M_writer(str(item.photo))
            __M_writer('"/>\r\n                    <br>\r\n                    <p class="product_name">\r\n                        <b>')
            __M_writer(str(item.name))
            __M_writer('</b>\r\n                    </p>\r\n                </a>\r\n                <br>\r\n                <p class="product_name">\r\n                    Sold by: ')
            __M_writer(str(item.manufacturer))
            __M_writer('\r\n                </p>\r\n                <br>\r\n                <p class="product_name">Qty on hand: ')
            __M_writer(str(item.quantity_on_hand))
            __M_writer('</p>\r\n                <br>\r\n                <p class="product_name">$')
            __M_writer(str(item.price))
            __M_writer('</p>\r\n            </div>\r\n')
        __M_writer('    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/index.html", "uri": "index.html", "line_map": {"64": 29, "65": 32, "66": 32, "67": 34, "68": 34, "69": 37, "75": 69, "27": 0, "35": 1, "45": 3, "52": 3, "53": 5, "54": 5, "55": 18, "56": 19, "57": 20, "58": 20, "59": 21, "60": 21, "61": 24, "62": 24, "63": 29}}
__M_END_METADATA
"""
