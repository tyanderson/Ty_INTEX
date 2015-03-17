# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426173383.292585
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/checkout.html'
_template_uri = '/checkout.html'
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
        __M_writer('\r\n\r\n    <div class="content">\r\n        <div class="col-md-8 col-md-offset-2">\r\n            <form method="POST">\r\n')
        for field in form:
            __M_writer('                <div class="col-sm-3"></div>\r\n                <div class="col-sm-9">\r\n                    ')
            __M_writer(str(field.errors))
            __M_writer('\r\n                </div>\r\n')
            if field.label=="First Name":
                __M_writer('                    <h2>Shipping Address</h2>\r\n')
            elif field.label=="Credit Card":
                __M_writer('                    <h2>Payment Information</h2>\r\n')
            __M_writer('                <div class="form-group">\r\n                    <label for=')
            __M_writer(str(field.name))
            __M_writer(' class="col-sm-3">')
            __M_writer(str(field.label))
            __M_writer('</label>\r\n                    <div class="col-sm-9" style="margin-bottom: 15px;">\r\n                        ')
            __M_writer(str(field))
            __M_writer('\r\n                    </div>\r\n                </div>\r\n')
        __M_writer('                <h1>REST API Example</h1>\r\n                <pre>\r\n                Endpoint: http://dithers.cs.byu.edu/iscore/api/v1/charges\r\n                Valid credit card: Visa, 4732817300654, Exp. 10/15, CVC 411, Cardholder Name: Cosmo Limesandal\r\n                Sample Charge Creation:\r\n                curl http://dithers.cs.byu.edu/iscore/api/v1/charges ')
        __M_writer('                -d apiKey=YOUR_API_KEY ')
        __M_writer('                -d currency=usd ')
        __M_writer('                -d amount=5.99 ')
        __M_writer('                -d type=Visa ')
        __M_writer('                -d number=4732817300654 ')
        __M_writer('                -d exp_month=10 ')
        __M_writer('                -d exp_year=15 ')
        __M_writer('                -d cvc=411 ')
        __M_writer('                -d "name=Cosmo Limesandal" ')
        __M_writer('                -d "description=Charge for cosmo@is411.byu.edu"\r\n                Query Charges:\r\n                curl --get http://dithers.cs.byu.edu/iscore/api/v1/charges ')
        __M_writer('                -d apiKey=YOUR_API_KEY\r\n                </pre>\r\n                <button type="button" class="btn btn-primary" id="charge">Charge</button>\r\n                <button type="button" class="btn btn-success" id="queryCharges">Query Charges</button>\r\n                <input type="text" id="chargeId">\r\n                <br />\r\n                <div id="message"></div>\r\n                <script>\r\n                    $(function(){})\r\n                </script>\r\n                <div class="form-group">\r\n                    <button style="float: right;" type="submit" class="btn btn-primary">Submit</button>\r\n                </div>\r\n            </form>\r\n        </div>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/checkout.html", "source_encoding": "ascii", "line_map": {"64": 19, "65": 19, "66": 21, "67": 21, "68": 25, "69": 31, "70": 32, "71": 33, "72": 34, "73": 35, "74": 36, "75": 37, "76": 38, "77": 39, "78": 40, "79": 43, "85": 79, "27": 0, "35": 1, "45": 3, "52": 3, "53": 8, "54": 9, "55": 11, "56": 11, "57": 13, "58": 14, "59": 15, "60": 16, "61": 18, "62": 19, "63": 19}, "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/checkout.html"}
__M_END_METADATA
"""
