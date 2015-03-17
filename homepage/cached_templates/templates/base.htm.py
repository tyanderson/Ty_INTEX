# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426518561.360296
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer', 'leftMenu', 'content', 'header', 'mainContent']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        len = context.get('len', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def leftMenu():
            return render_leftMenu(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def mainContent():
            return render_mainContent(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<html !DOCTYPE>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n        <title>Colonial Heritage Foundation</title>\r\n\r\n')
        __M_writer('        <script src="/static/homepage/scripts/jquery.js"></script>\r\n        <script src="/static/homepage/scripts/jquery.form.min.js"></script>\r\n\r\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n        <!-- Latest compiled and minified CSS -->\r\n        <link rel="stylesheet" href="/static/homepage/styles/bootstrap.min.css">\r\n        <!-- Optional theme -->\r\n        <link rel="stylesheet" href="/static/homepage/styles/Bootstrap-theme.css">\r\n\r\n        <!-- Latest compiled and minified CSS -->\r\n        <!-- glyphicons -->\r\n        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\r\n\r\n        <!-- Latest compiled and minified JavaScript -->\r\n        <script src="/static/homepage/scripts/Bootstrap.js"></script>\r\n\r\n        <!-- Favicon -->\r\n        <link rel="icon" type="image/x-icon" href="http://wangweiqiang.net/demo/MagicNote/images/quill.png" />\r\n\r\n')
        if request.user.groups.filter(name="Admin"):
            if request.get_full_path()=="/":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
            elif request.get_full_path()=="/homepage":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
            elif request.get_full_path()=="/homepage/":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
            elif request.get_full_path()=="/homepage/index":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
            elif request.get_full_path()=="/homepage/index/":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
            elif request.get_full_path()=="/homepage/index.htm":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
        elif request.user.groups.filter(name="Manager"):
            if request.get_full_path()=="/":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
            elif request.get_full_path()=="/homepage":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
            elif request.get_full_path()=="/homepage/":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
            elif request.get_full_path()=="/homepage/index":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
            elif request.get_full_path()=="/homepage/index/":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
            elif request.get_full_path()=="/homepage/index.htm":
                __M_writer('                <meta http-equiv="REFRESH" content="0;url=http://localhost:8000/homepage/users">\r\n')
        __M_writer('    </head>\r\n    <body>\r\n        <header>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n        </header>\r\n\r\n        <!-- Contents -->\r\n        <div class="container content">\r\n            <!-- Left Content -->\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'leftMenu'):
            context['self'].leftMenu(**pageargs)
        

        __M_writer('\r\n\r\n            <!-- Center Content -->\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n            <!-- Main Content -->\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainContent'):
            context['self'].mainContent(**pageargs)
        

        __M_writer('\r\n            <!-- Login Modal -->\r\n            <div class="modal fade" id="login_form" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n                <div class="modal-dialog">\r\n                    <form method="POST" action="/homepage/login" class="form-horizontal">\r\n                        <div class="modal-content">\r\n                            <div class="modal-header">\r\n                                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n                                <h4 class="modal-title" id="myModalLabel">Login</h4>\r\n                            </div>\r\n                            <div class="modal-body">\r\n                                <img src="/static/homepage/media/loading.gif" class="loading"/>\r\n                            </div>\r\n                            <div class="modal-footer">\r\n                                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n                                <button type="submit" class="btn btn-primary">Submit</button>\r\n                            </div>\r\n                        </div>\r\n                    </form>\r\n                </div>\r\n            </div>\r\n            <!-- Cart Modal -->\r\n            <div class="modal fade" id="cart_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n                <div class="modal-dialog">\r\n                    <form method="POST" action="/homepage/login" class="form-horizontal">\r\n                        <div class="modal-content">\r\n                            <div class="modal-header">\r\n                                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n                                <h4 class="modal-title" id="myModalLabel">Shopping Cart</h4>\r\n                            </div>\r\n                            <div class="modal-body">\r\n                                <img src="/static/homepage/media/loading.gif" class="loading"/>\r\n                            </div>\r\n                            <div class="modal-footer">\r\n                                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n                                <a href="/store/checkout"><button type="button" class="btn btn-primary">Checkout</button></a>\r\n                            </div>\r\n                        </div>\r\n                    </form>\r\n                </div>\r\n            </div>\r\n        </div>\r\n\r\n        <!-- Footer -->\r\n        <footer>\r\n            <div class="container">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </footer>\r\n\r\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n    </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    <p>Copyright 2015, All Rights Reserved</p>\r\n                    <p>Colonial Heritage Foundation</p>\r\n                    <p>Website by <a href="mailto:ty.anderson.3@gmail.com">Ty Anderson</a></p>\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_leftMenu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def leftMenu():
            return render_leftMenu(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n            <!-- Navigation Bar -->\r\n            <nav class="navbar navbar-inverse">\r\n                <!-- Cart corner -->\r\n                <div class="col-md-offset-10 col-md-2" id="cart_corner">\r\n                    <div class="col-sm-9">\r\n                        <a href="#" id="cart_button">\r\n                            <div class="cart">\r\n                                <p>\r\n')
        if 'shopping_cart' in request.session:
            __M_writer('                                        ')
            __M_writer(str(len(request.session['shopping_cart'])))
            __M_writer(' Items\r\n')
        else:
            __M_writer('                                        0 Items\r\n')
        __M_writer('                                </p>\r\n                                <span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span>\r\n                            </div>\r\n                        </a>\r\n                        <div id="login_corner">\r\n')
        if request.user.is_authenticated():
            __M_writer('                                <p>\r\n                                    <a href="/homepage/account" id="hello" class="login_link">\r\n                                        Hello, ')
            __M_writer(str(request.user.first_name))
            __M_writer('\r\n                                    </a>\r\n                                </p>\r\n                                <br>\r\n                                <p><a href="/homepage/login.logoutUser" id="logout" class="login_link">Logout</a></p>\r\n')
        else:
            __M_writer('                                <p><a href="#" class="login_link" id="login">Login</a></p>\r\n                                <p><a href="/homepage/users.create" class="login_link">Create Account</a></p>\r\n')
        __M_writer('                        </div>\r\n                    </div>\r\n                </div>\r\n                <!-- Brand and toggle get grouped for better mobile display -->\r\n                <div class="navbar-header">\r\n                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n                        <span class="sr-only">Toggle navigation</span>\r\n                        <span class="icon-bar"></span>\r\n                        <span class="icon-bar"></span>\r\n                        <span class="icon-bar"></span>\r\n                    </button>\r\n                    <a href="/homepage/index" id="logo">\r\n                        <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/quill.png" width="150px" />\r\n                        <span id="logo_name" style="position:relative;left:-50px;">CHF</span>\r\n                        <!--<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/CHFLogo.png" />-->\r\n                    </a>\r\n                 </div>\r\n\r\n                <!-- Collect the nav links, forms, and other content for toggling -->\r\n                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n                    <ul class="nav navbar-nav items">\r\n')
        if request.user.groups.filter(name="Admin"):
            __M_writer('                        <!-- Users link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_page=="users":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/homepage/users" class="menuitem">Users <span class="sr-only">(current)</span></a></li>\r\n                        <!-- Inventory link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_page=="inventory":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/homepage/inventory" class="menuitem">Inventory <span class="sr-only">(current)</span></a></li>\r\n                        <!-- Rentals link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_page=="rentableItems":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/homepage/rentableItems" class="menuitem">Rentable Items <span class="sr-only">(current)</span></a></li>\r\n                        <!-- Events link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_page=="events":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/homepage/events" class="menuitem">Events <span class="sr-only">(current)</span></a></li>\r\n')
        elif request.user.groups.filter(name="Manager"):
            __M_writer('                        <!-- Users link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_page=="users":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/homepage/users" class="menuitem">Users <span class="sr-only">(current)</span></a></li>\r\n                        <!-- Inventory link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_page=="inventory":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/homepage/inventory" class="menuitem">Inventory <span class="sr-only">(current)</span></a></li>\r\n                        <!-- Rentals link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_page=="rentableItems":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/homepage/rentableItems" class="menuitem">Rentable Items <span class="sr-only">(current)</span></a></li>\r\n                        <!-- Events link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_page=="events":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/homepage/events" class="menuitem">Events <span class="sr-only">(current)</span></a></li>\r\n')
        else:
            __M_writer('                        <!-- Store link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_app=="store":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/store/index" class="menuitem">Store <span class="sr-only">(current)</span></a></li>\r\n                        <!-- About link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_page=="about":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/homepage/about" class="menuitem">About <span class="sr-only">(current)</span></a></li>\r\n                        <!-- Terms link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_page=="terms":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/homepage/terms" class="menuitem">Terms</a></li>\r\n                        <!-- Contact link ----------------------------------------------------------------------------------------->\r\n')
            if request.dmp_router_page=="contact":
                __M_writer('                                ')
                __M_writer(str("<li class='active'>"))
                __M_writer('\r\n')
            else:
                __M_writer('                                ')
                __M_writer(str("<li>"))
                __M_writer('\r\n')
            __M_writer('                            <a href="/homepage/contact" class="menuitem">Contact</a></li>\r\n')
        __M_writer('                    </ul>\r\n                </div><!-- /.navbar-collapse -->\r\n            </nav>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def mainContent():
            return render_mainContent(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 4, "18": 0, "37": 2, "38": 4, "39": 5, "43": 5, "44": 14, "45": 18, "46": 18, "47": 18, "48": 35, "49": 36, "50": 37, "51": 38, "52": 39, "53": 40, "54": 41, "55": 42, "56": 43, "57": 44, "58": 45, "59": 46, "60": 47, "61": 49, "62": 50, "63": 51, "64": 52, "65": 53, "66": 54, "67": 55, "68": 56, "69": 57, "70": 58, "71": 59, "72": 60, "73": 61, "74": 64, "79": 210, "84": 216, "89": 219, "94": 222, "99": 272, "100": 277, "101": 277, "102": 277, "108": 268, "114": 268, "120": 216, "131": 219, "142": 67, "151": 67, "152": 76, "153": 77, "154": 77, "155": 77, "156": 78, "157": 79, "158": 81, "159": 86, "160": 87, "161": 89, "162": 89, "163": 94, "164": 95, "165": 98, "166": 110, "167": 110, "168": 112, "169": 112, "170": 119, "171": 120, "172": 121, "173": 122, "174": 122, "175": 122, "176": 123, "177": 124, "178": 124, "179": 124, "180": 126, "181": 128, "182": 129, "183": 129, "184": 129, "185": 130, "186": 131, "187": 131, "188": 131, "189": 133, "190": 135, "191": 136, "192": 136, "193": 136, "194": 137, "195": 138, "196": 138, "197": 138, "198": 140, "199": 142, "200": 143, "201": 143, "202": 143, "203": 144, "204": 145, "205": 145, "206": 145, "207": 147, "208": 148, "209": 149, "210": 150, "211": 151, "212": 151, "213": 151, "214": 152, "215": 153, "216": 153, "217": 153, "218": 155, "219": 157, "220": 158, "221": 158, "222": 158, "223": 159, "224": 160, "225": 160, "226": 160, "227": 162, "228": 164, "229": 165, "230": 165, "231": 165, "232": 166, "233": 167, "234": 167, "235": 167, "236": 169, "237": 171, "238": 172, "239": 172, "240": 172, "241": 173, "242": 174, "243": 174, "244": 174, "245": 176, "246": 177, "247": 178, "248": 179, "249": 180, "250": 180, "251": 180, "252": 181, "253": 182, "254": 182, "255": 182, "256": 184, "257": 186, "258": 187, "259": 187, "260": 187, "261": 188, "262": 189, "263": 189, "264": 189, "265": 191, "266": 193, "267": 194, "268": 194, "269": 194, "270": 195, "271": 196, "272": 196, "273": 196, "274": 198, "275": 200, "276": 201, "277": 201, "278": 201, "279": 202, "280": 203, "281": 203, "282": 203, "283": 205, "284": 207, "290": 222, "301": 290}, "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2\\homepage\\templates/base.htm", "uri": "base.htm"}
__M_END_METADATA
"""
