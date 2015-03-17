# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425436532.323142
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/item.html'
_template_uri = 'item.html'
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
        photos = context.get('photos', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        catalog_items = context.get('catalog_items', UNDEFINED)
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
        photos = context.get('photos', UNDEFINED)
        def content():
            return render_content(context)
        catalog_items = context.get('catalog_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="col-md-8">\r\n            ')
        a=0 
        
        __M_writer('\r\n')
        for item in catalog_items:
            __M_writer('                <div class="col-md-3 item_display">\r\n                    <a href="/store/item.view/')
            __M_writer(str(item.id))
            __M_writer('">\r\n                        <img class="item_photo" src="/static')
            __M_writer(str(photos[a].image))
            __M_writer('"/>\r\n                        <br>\r\n                        <p class="product_name">\r\n                            ')
            __M_writer(str(item.name))
            __M_writer('\r\n                        </p>\r\n                    </a>\r\n                    <p class="price">$')
            __M_writer(str(item.price))
            __M_writer('</p>\r\n                </div>\r\n                ')
            a+=1 
            
            __M_writer('\r\n')
        __M_writer('        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "item.html", "line_map": {"64": 13, "65": 13, "66": 16, "27": 0, "36": 1, "70": 18, "68": 18, "71": 20, "77": 71, "46": 3, "67": 16, "54": 3, "55": 6, "57": 6, "58": 7, "59": 8, "60": 9, "61": 9, "62": 10, "63": 10}, "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/item.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
