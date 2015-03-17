# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426519729.581763
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2/store/templates/left_col.html'
_template_uri = '/store/templates/left_col.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!-- <div class="col-md-3" id="left_col"> -->\r\n<ul class="left_bar">\r\n    <lh class="lh">Sale Items</lh>\r\n    <li>Mass-Produced</li>\r\n</ul>\r\n<ul class="left_bar">\r\n    <lh class="lh">Rental Items</lh>\r\n    <li>Men</li>\r\n    <li>Women</li>\r\n    <li>Kids</li>\r\n</ul>\r\n<!-- </div> -->')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/store/templates/left_col.html", "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2/store/templates/left_col.html", "line_map": {"16": 0, "27": 21, "21": 1}, "source_encoding": "ascii"}
__M_END_METADATA
"""
