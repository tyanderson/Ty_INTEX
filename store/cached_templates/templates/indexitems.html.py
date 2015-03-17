# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425790848.161591
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/indexitems.html'
_template_uri = 'indexitems.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        catalog_items = context.get('catalog_items', UNDEFINED)
        __M_writer = context.writer()
        for item in catalog_items:
            __M_writer('    <div class="col-md-3 item_display">\r\n        <a href="/store/index.itemview/')
            __M_writer(str(item.id))
            __M_writer('">\r\n            <img class="item_photo" src="/static')
            __M_writer(str(item.photo))
            __M_writer('"/>\r\n            <br>\r\n            <p class="product_name">\r\n                ')
            __M_writer(str(item.name))
            __M_writer('\r\n            </p>\r\n        </a>\r\n        <p class="price">$')
            __M_writer(str(item.price))
            __M_writer('</p>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"37": 31, "16": 0, "22": 1, "23": 2, "24": 3, "25": 3, "26": 4, "27": 4, "28": 7, "29": 7, "30": 10, "31": 10}, "uri": "indexitems.html", "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/indexitems.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
