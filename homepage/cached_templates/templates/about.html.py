# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425399495.828034
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/about.html'
_template_uri = 'about.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n<div class="col-md-12 centerContent">\r\n    <h1>About Us</h1>\r\n    <center>\r\n        <img src="http://1.bp.blogspot.com/-ecEtKJ8mcx0/Umxoi_a1duI/AAAAAAAAAIM/Un-GZ_F6I4g/s320/IMG_20131026_111903_044.jpg">\r\n        <p>\r\n            Well, we no know no black sheep wall.\r\n        </p>\r\n    </center>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/about.html", "source_encoding": "ascii", "uri": "about.html"}
__M_END_METADATA
"""
