# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426198173.669392
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
        __M_writer('<!-- <div class="col-md-3" id="left_col"> -->\r\n<h4>Clothing</h4>\r\n<h5>Men</h5>\r\n<h5>Women</h5>\r\n<h5>Children</h5>\r\n<!-- </div> -->')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2/store/templates/left_col.html", "uri": "/store/templates/left_col.html", "line_map": {"16": 0, "27": 21, "21": 1}}
__M_END_METADATA
"""
