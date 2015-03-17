# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425399004.369044
_enable_loop = True
_template_filename = 'C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'leftMenu', 'mainContent', 'header', 'footer']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def leftMenu():
            return render_leftMenu(context._locals(__M_locals))
        def mainContent():
            return render_mainContent(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<html !DOCTYPE>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n        <title>Colonial Heritage Foundation</title>\r\n\r\n')
        __M_writer('        <script src="/static/homepage/scripts/jquery.js"></script>\r\n\r\n')
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
        

        __M_writer('\r\n        </header>\r\n\r\n        <!-- Contents -->\r\n        <div class="container content">\r\n\r\n            <!-- Left Content -->\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'leftMenu'):
            context['self'].leftMenu(**pageargs)
        

        __M_writer('\r\n\r\n            <!-- Center Content -->\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n            <!-- Main Content -->\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainContent'):
            context['self'].mainContent(**pageargs)
        

        __M_writer('\r\n\r\n        </div>\r\n\r\n        <!-- Footer -->\r\n        <footer>\r\n            <div class="container">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </footer>\r\n\r\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n    </body>\r\n</html>')
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


def render_leftMenu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def leftMenu():
            return render_leftMenu(context)
        __M_writer = context.writer()
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


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n            <!-- Navigation Bar -->\r\n            <nav class="navbar navbar-inverse">\r\n                <div class="container">\r\n                    <!-- Cart corner -->\r\n                    <div class="col-md-offset-8 col-md-2" id="cart_corner">\r\n                        <div class="col-sm-9">\r\n                            <a href="/homepage/cart/">\r\n                                <div class="cart">\r\n                                    <p>0 Items</p>\r\n                                    <span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span>\r\n                                </div>\r\n                            </a>\r\n                            <div id="login">\r\n')
        if request.user.is_authenticated():
            __M_writer('                                    <p><a href="/homepage/account" id="login">\r\n                                        Hello, ')
            __M_writer(str(request.user))
            __M_writer('</a>\r\n                                    </p>\r\n                                    <p><a href="/homepage/login.logoutUser" id="login">Logout</a></p>\r\n')
        else:
            __M_writer('                                    <p><a href="/homepage/login" id="login">Login</a></p>\r\n')
        __M_writer('                            </div>\r\n                        </div>\r\n                    </div>\r\n                    <!-- Brand and toggle get grouped for better mobile display -->\r\n                    <div class="navbar-header">\r\n                        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n                            <span class="sr-only">Toggle navigation</span>\r\n                            <span class="icon-bar"></span>\r\n                            <span class="icon-bar"></span>\r\n                            <span class="icon-bar"></span>\r\n                        </button>\r\n                        <a href="/homepage/index" id="logo">\r\n                            <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/quill.png" width="150px" />\r\n                            <span id="logo_name" style="position:relative;left:-50px;">CHF</span>\r\n                            <!--<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/CHFLogo.png" />-->\r\n                        </a>\r\n                     </div>\r\n\r\n                <!-- Collect the nav links, forms, and other content for toggling -->\r\n                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n                    <ul class="nav navbar-nav items">\r\n')
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
        __M_writer('                    </ul>\r\n                </div><!-- /.navbar-collapse -->\r\n              </div><!-- /.container-fluid -->\r\n            </nav>\r\n            <div class="container" id="search_bar">\r\n                <ul class="nav navbar-nav navbar-right" id="navbar-right">\r\n                    <form class="navbar-form navbar-left" role="search">\r\n                        <div class="form-group">\r\n                            <input type="text" class="form-control" placeholder="Search">\r\n                        </div>\r\n                        <button type="submit" class="btn btn-primary">Submit</button>\r\n                    </form>\r\n                </ul>\r\n            </div>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n                <p>Copyright 2015, All Rights Reserved</p>\r\n                <p>Colonial Heritage Foundation</p>\r\n                <p>Website by <a href="mailto:ty.anderson.3@gmail.com">Ty Anderson</a></p>\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/homepage/templates/base.htm", "line_map": {"16": 4, "18": 0, "36": 2, "37": 4, "38": 5, "42": 5, "43": 14, "44": 17, "45": 17, "46": 17, "47": 34, "48": 35, "49": 36, "50": 37, "51": 38, "52": 39, "53": 40, "54": 41, "55": 42, "56": 43, "57": 44, "58": 45, "59": 46, "60": 48, "61": 49, "62": 50, "63": 51, "64": 52, "65": 53, "66": 54, "67": 55, "68": 56, "69": 57, "70": 58, "71": 59, "72": 60, "73": 63, "78": 211, "83": 218, "88": 221, "93": 224, "98": 235, "99": 240, "100": 240, "101": 240, "107": 221, "118": 218, "129": 224, "140": 66, "148": 66, "149": 80, "150": 81, "151": 82, "152": 82, "153": 85, "154": 86, "155": 88, "156": 100, "157": 100, "158": 102, "159": 102, "160": 109, "161": 110, "162": 111, "163": 112, "164": 112, "165": 112, "166": 113, "167": 114, "168": 114, "169": 114, "170": 116, "171": 118, "172": 119, "173": 119, "174": 119, "175": 120, "176": 121, "177": 121, "178": 121, "179": 123, "180": 125, "181": 126, "182": 126, "183": 126, "184": 127, "185": 128, "186": 128, "187": 128, "188": 130, "189": 132, "190": 133, "191": 133, "192": 133, "193": 134, "194": 135, "195": 135, "196": 135, "197": 137, "198": 138, "199": 139, "200": 140, "201": 141, "202": 141, "203": 141, "204": 142, "205": 143, "206": 143, "207": 143, "208": 145, "209": 147, "210": 148, "211": 148, "212": 148, "213": 149, "214": 150, "215": 150, "216": 150, "217": 152, "218": 154, "219": 155, "220": 155, "221": 155, "222": 156, "223": 157, "224": 157, "225": 157, "226": 159, "227": 161, "228": 162, "229": 162, "230": 162, "231": 163, "232": 164, "233": 164, "234": 164, "235": 166, "236": 167, "237": 168, "238": 169, "239": 170, "240": 170, "241": 170, "242": 171, "243": 172, "244": 172, "245": 172, "246": 174, "247": 176, "248": 177, "249": 177, "250": 177, "251": 178, "252": 179, "253": 179, "254": 179, "255": 181, "256": 183, "257": 184, "258": 184, "259": 184, "260": 185, "261": 186, "262": 186, "263": 186, "264": 188, "265": 190, "266": 191, "267": 191, "268": 191, "269": 192, "270": 193, "271": 193, "272": 193, "273": 195, "274": 197, "280": 231, "286": 231, "292": 286}, "filename": "C:\\Users\\Charizard\\Google Drive\\BYU\\IS 413\\Sprint2/homepage/templates/base.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
