# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425772594.022998
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/index.itemview.html'
_template_uri = 'index.itemview.html'
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
        photo = context.get('photo', UNDEFINED)
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
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
        photo = context.get('photo', UNDEFINED)
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="col-md-6">\r\n            <img src="/static')
        __M_writer(str(photo.image))
        __M_writer('" class="itemview_image"/>\r\n        </div>\r\n        <div class="col-md-6">\r\n            <h2>')
        __M_writer(str(item.name))
        __M_writer('</h2>\r\n            <p><b>Serial: </b>')
        __M_writer(str(item.serial_number))
        __M_writer('</p>\r\n            <p><b>Description: </b>')
        __M_writer(str(item.description))
        __M_writer('</p>\r\n')
        if item.clothing_detail_id:
            __M_writer('                ')
            __M_writer(str(item.clothing_detail_id))
            __M_writer('\r\n')
        __M_writer('            <p><b>Price: </b>$')
        __M_writer(str(item.price))
        __M_writer('</p>\r\n            <p><b>Quantity available: </b>')
        __M_writer(str(item.quantity_on_hand))
        __M_writer('</p>\r\n')
        if item.quantity_on_hand:
            if item.quantity_on_hand>0:
                __M_writer('            <form class="form-horizontal">\r\n                <div class="form-group">\r\n                    <label for="qty" class="col-sm-2 control-label">Quantity</label>\r\n                    <div class="col-sm-5">\r\n                        <select class="form-control" id="quantity" style="width:70px;">\r\n\r\n                                <option value="1" selected>1</option>\r\n')
                if item.quantity_on_hand>1:
                    __M_writer('                                    ')
                    i = 2 
                    
                    __M_writer('\r\n')
                    for j in range(item.quantity_on_hand-1):
                        __M_writer('                                        <option value="')
                        __M_writer(str(i))
                        __M_writer('">')
                        __M_writer(str(i))
                        __M_writer('</option>\r\n                                        ')
                        i+=1 
                        
                        __M_writer('\r\n')
                        if i==6:
                            __M_writer('                                            ')
                            break 
                            
                            __M_writer('\r\n')
            else:
                __M_writer('                                <option value="0" selected>Out of stock</option>\r\n')
        __M_writer('                        </select>\r\n                        <p style="display:none;" id="item_id">')
        __M_writer(str(item.id))
        __M_writer('</p>\r\n                    </div>\r\n                </div>\r\n')
        if item.quantity_on_hand:
            if item.quantity_on_hand>0:
                __M_writer('                        <div class="form-group">\r\n                            <div class="col-sm-offset-2 col-sm-10">\r\n                                <button type="button" class="btn btn-warning" data-item_id="')
                __M_writer(str(item.id))
                __M_writer('" id="add_to_cart">Add to Cart</button>\r\n                            </div>\r\n                        </div>\r\n')
        __M_writer('            </form>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "37": 1, "47": 3, "56": 3, "57": 6, "58": 6, "59": 9, "60": 9, "61": 10, "62": 10, "63": 11, "64": 11, "65": 12, "66": 13, "67": 13, "68": 13, "69": 15, "70": 15, "71": 15, "72": 16, "73": 16, "74": 17, "75": 18, "76": 19, "77": 26, "78": 27, "79": 27, "81": 27, "82": 28, "83": 29, "84": 29, "85": 29, "86": 29, "87": 29, "88": 30, "90": 30, "91": 31, "92": 32, "93": 32, "95": 32, "96": 36, "97": 37, "98": 40, "99": 41, "100": 41, "101": 44, "102": 45, "103": 46, "104": 48, "105": 48, "106": 53, "112": 106}, "uri": "index.itemview.html", "source_encoding": "ascii", "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\store\\templates/index.itemview.html"}
__M_END_METADATA
"""
