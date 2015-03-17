# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425450156.23616
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/contact.html'
_template_uri = 'contact.html'
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
        __M_writer('\r\n<div class="col-md-12 centerContent">\r\n    <h1>Contact Us</h1>\r\n    <div class="col-md-6">\r\n        <form class="contact">\r\n            <div class="form-group">\r\n                <label for="name">Name</label>\r\n                <input type="text" class="form-control" id="name" placeholder="Name">\r\n            </div>\r\n            <div class="form-group">\r\n                <label for="email">Email address</label>\r\n                <input type="email" class="form-control" id="email" placeholder="Enter email">\r\n            </div>\r\n            <div class="form-group">\r\n                <label for="contacttype">Contact type</label>\r\n                <select class="form-control" id="contacttype">\r\n                    <option>Question</option>\r\n                    <option>Complaint</option>\r\n                    <option>Comment</option>\r\n                </select>\r\n            </div>\r\n            <div class="form-group">\r\n                <label for="message">Your message</label>\r\n                <textarea class="form-control" id="message" rows="3"></textarea>\r\n            </div>\r\n            <button type="submit" class="btn btn-success">Submit</button>\r\n        </form>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "contact.html", "source_encoding": "ascii", "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/contact.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}}
__M_END_METADATA
"""
