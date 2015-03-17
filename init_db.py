#!/user/bin/env python

# Initialize django
import os
import sys
import random
import datetime
from decimal import Decimal
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'Sprint2.settings'
django.setup()

import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess

# DROP DATABASE, RECREATE IT, THEN MIGRATE IT #

__author__ = 'Group1-3'
cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])


#           CREATE PERMISSIONS/GROUPS           #

for data in [{'codename': 'manager_rights', 'name': 'Has Manager Rights'},
             {'codename': 'customer_rights', 'name': 'Has Customer Rights'},
             {'codename': 'admin_rights', 'name': 'Has Administrator Rights'}]:
    p = Permission()
    for k, v in data.items():
        setattr(p, k, v)
        p.content_type = ContentType.objects.get(id=2)
    p.save()

for data in [{'name': 'Customer'}, {'name': 'Manager'}, {'name': 'Admin'}]:
    g = Group()
    for k, v in data.items():
        setattr(g, k, v)
        g.save()
        if k == 'name':
            p = Permission.objects.get(codename=v.lower() + '_rights')
            g.permissions.add(p)


print('Permissions initialized')


#           CREATE ADRESSES        #

for data in [
    {'address1':    '89 E 200 N',
     'city':        'Orem',
     'state':       'UT',
     'zip_code':    '84602'},
    {'address1':    '143 Ethyl Ct. #3',
     'city':        'Milpitas',
     'state':       'CA',
     'zip_code':    '95035'},
    {'address1':    '79 E 300 N',
     'city':        'Provo',
     'state':       'UT',
     'zip_code':    '84606'}
]:

    a = hmod.Address()
    for k, v in data.items():
        setattr(a, k, v)
    a.save()

print('Addresses initialized')


#           CREATE PHOTOS          #

for data in [
    ["Wand", "/store/media/wand.jpg"],
    ["GoveRobes", "/store/media/gove.jpg"],
    ["Quill", "/store/media/quill.jpg"],
]:
    # Create new Sale Product
    p = hmod.Photograph()

    # Assign product attributes
    p.description = data[0]
    p.image = data[1]
    p.save()

print('Photos initialized')


#           CREATE USERS           #

for data in [
    {'username':        'TyCool4School',
     'email':           'ty@gmail.com',
     'first_name':      'Ty',
     'last_name':       'Anderson'},
    {'username':        'CodyingAllNight',
     'email':           'cdy@gmail.com',
     'first_name':      'Cody',
     'last_name':       'Booher'},
]:

    u = hmod.User()
    for k, v in data.items():
        setattr(u, k, v)
    u.set_password('p')
    u.address = hmod.Address.objects.get(address1='79 E 300 N')
    u.save()
    Group.objects.get(name='Customer').user_set.add(u)

print('Users initialized')


#           CREATE EMPLOYEES            #

for data in [
    {'username':        'Kevbo',
     'email':           'k@gmail.com',
     'first_name':      'Kevin',
     'last_name':       'Gardner',
     'is_superuser':    'TRUE',
     'is_staff':        'TRUE',
     'date_hired':      datetime.datetime.now(),
     'salary':          65400.00},
    {'username':        'Reverend',
     'email':           'r@gmail.com',
     'first_name':      'Rebecca',
     'last_name':       'Gardner',
     'is_superuser':    'FALSE',
     'is_staff':        'TRUE',
     'date_hired':      datetime.datetime.now(),
     'wage':            32.45}
]:

    e = hmod.Employee()
    for k, v in data.items():
        setattr(e, k, v)
    e.set_password('p')
    e.address = hmod.Address.objects.get(address1='143 Ethyl Ct. #3')
    e.save()
    if e.username == 'Kevbo':
        Group.objects.get(name='Admin').user_set.add(e)
    else:
        Group.objects.get(name='Manager').user_set.add(e)

print('Employees initialized')


#           CREATE VENDORS            #

for data in [
    {'username':        '2Tyler2Quit',
     'email':           'tyler@gmail.com',
     'first_name':      'Tyler',
     'last_name':       'White',
     'SSN':             '234-45-6789',
     'EIN':             '12-3456789',
     'UTTaxID':         'AF-2345'},
    {'username':        'GoveByDaPound',
     'email':           'gove@gmail.com',
     'first_name':      'Gove',
     'last_name':       'Allen',
     'SSN':             '224-45-6789',
     'EIN':             '12-3456789',
     'UTTaxID':         'AF-2345'}
]:

    ven = hmod.Vendor()
    for k, v in data.items():
        setattr(ven, k, v)
    ven.set_password('p')
    ven.address = hmod.Address.objects.get(address1='89 E 200 N')
    ven.save()

print('Vendors initialized')


#           CREATE TRANSACTIONS           #

for data in [
    {'date':                    datetime.date.today() - datetime.timedelta(2),
     'phone':                   '801-263-9250',
     'date_paid':               datetime.date.today() - datetime.timedelta(2),
     'date_packed':             datetime.date.today() - datetime.timedelta(1),
     'date_shipped':            datetime.date.today(),
     'tracking_number':         '12324356u5634',
     'customer_id':             hmod.User.objects.get(username='2Tyler2Quit').id,
     'shipped_by':              hmod.User.objects.get(username='Reverend'),
     'handled_by':              hmod.User.objects.get(username='Reverend'),
     'ships_to':                hmod.User.objects.get(username='2Tyler2Quit').address,
     'payment_processed_by':    hmod.User.objects.get(username='Reverend')},
    {'date':                    datetime.date.today() - datetime.timedelta(3),
     'phone':                   '801-245-5678',
     'date_paid':               datetime.date.today() - datetime.timedelta(2),
     'customer_id':             hmod.User.objects.get(username='CodyingAllNight').id,
     'payment_processed_by':    hmod.User.objects.get(username='Reverend')},
    {'date':                    datetime.date.today() - datetime.timedelta(3),
     'phone':                   '801-456-6456',
     'date_paid':               datetime.date.today() - datetime.timedelta(3),
     'customer_id':             hmod.User.objects.get(username='Kevbo').id,
     'payment_processed_by':    hmod.User.objects.get(username='Kevbo')},
    {'date':                    datetime.date.today() - datetime.timedelta(4),
     'phone':                   '801-345-1122',
     'date_paid':               datetime.date.today() - datetime.timedelta(4),
     'customer_id':             hmod.User.objects.get(username='TyCool4School').id,
     'payment_processed_by':    hmod.User.objects.get(username='Kevbo')},
    {'date':                    datetime.date.today(),
     'phone':                   '801-345-1122',
     'date_paid':               datetime.date.today(),
     'customer_id':             hmod.User.objects.get(username='TyCool4School').id,
     'payment_processed_by':    hmod.User.objects.get(username='Kevbo')}

]:

    t = hmod.Transaction()
    for k, v in data.items():
        setattr(t, k, v)
    t.save()

print('Transactions initialized')


#              CREATE CATEGORIES            #

for data in [{'name': 'Woodworking'}, {'name': 'Clothing'}, {'name': 'Quills'}]:

    c = hmod.Category()
    for k, v in data.items():
        setattr(c, k, v)
    c.save()

print('Categories initialized')


#          CREATE CLOTHING DETAILS        #

for data in [{'size': 'Large', 'gender': 'M', 'color': 'Periwinkle'}]:

    cd = hmod.Clothing_Detail()
    for k, v in data.items():
        setattr(cd, k, v)
    cd.save()

print('Clothing Details initialized')


#           CREATE ITEMS            #

for data in [
    {'name':                "Model Mayflower",
     'description':         "A scale model of the goodship Mayflower.",
     'serial_number':       "M0001",
     'value':               4000.00,
     'creator':             hmod.User.objects.get(username='TyCool4School'),
     'photo_id':            3}
]:

    i = hmod.Item()
    for k, v in data.items():
        setattr(i, k, v)
    i.save()

print('Items initialized')


#           CREATE SALE PRODUCTS            #

for data in [
    {'quantity_on_hand':    "10",
     'shelf_location':      "C-10.5",
     'production_time':     "10",
     'price':               10,
     'manufacturer':        "Harry Potter",
     'name':                "Wand",
     'description':         "Wand used in filming of Harry Potter.",
     'serial_number':       "C7415",
     'value':               4.00,
     'photo_id':            1},
    {'quantity_on_hand':    "100",
     'shelf_location':      "C-7.1",
     'production_time':     "5",
     'price':               4.99,
     'manufacturer':        "Maker Inc.",
     'name':                "Quill",
     'description':         "A fine feathered font-formatting device.",
     'serial_number':       "C4111",
     'value':               0.99,
     'photo_id':            3}
]:

    sp = hmod.Sale_Product()
    for k, v in data.items():
        setattr(sp, k, v)
    sp.save()

print('Sale Products initialized')


#           CREATE CUSTOM PRODUCTS            #

for data in [
    {'production_time':     "13",
     'price':               35.00,
     'name':                "Embroidered Hankerchief",
     'description':         "A finely made cotton hankerchief that can be decorated with a monogram or message.",
     'serial_number':       "C9349",
     'value':               4.00,
     'creator':             hmod.Vendor.objects.get(username='2Tyler2Quit'),
     'required_info':       'The message to be sewn into the hankerchief',
     'photo_id':            3}
]:

    cp = hmod.Custom_Product()
    for k, v in data.items():
        setattr(cp, k, v)
    cp.save()

print('Custom Products initialized')


#           CREATE ORDER FORMS            #

for data in [
    {'customer_info':
        'I admire you deeply and enjoy our long walks together on the beach. May this hankerchief ever remind you of me.'}
]:

    of = hmod.Order_Form()
    for k, v in data.items():
        setattr(of, k, v)
    of.save()

print('Order Forms initialized')


#           CREATE SALE ITEMS           #

for data in [
    {'transaction_id':  hmod.Transaction.objects.get(customer_id=hmod.User.objects.get(username='CodyingAllNight')).id,
     'amount':          35.00,
     'quantity':        1,
     'product_id':      hmod.Custom_Product.objects.first().id,
     'order_form_id':   hmod.Order_Form.objects.first().id},
    {'transaction_id':  hmod.Transaction.objects.get(customer_id=hmod.User.objects.get(username='2Tyler2Quit')).id,
     'amount':          15.00,
     'quantity':        3,
     'product_id':      hmod.Sale_Product.objects.get(name='Quill').id}
]:

    si = hmod.Sale_Item()
    for k, v in data.items():
        setattr(si, k, v)
    si.save()

print('Sale Items initialized')


#           CREATE RENTABLE ARTICLES          #

for data in [
    {'quantity_on_hand':    "1",
     'shelf_location':      "D-5.1",
     'name':                "Robes of Sir Gove",
     'description':         "Professor Gove's very own robe.",
     'serial_number':       "R4516",
     'value':               184.99,
     'owner':               hmod.User.objects.get(username='GoveByDaPound'),
     'photo_id':            2,
     'clothing_detail_id':  hmod.Clothing_Detail.objects.first().id,
     'price_per_day':       18.99},
    {'quantity_on_hand':    "0",
     'shelf_location':      "C-3.1",
     'name':                "Colonial Musket",
     'description':         "Authentic. Appears to have been dropped. Never fired.",
     'serial_number':       "R3256",
     'value':               2304.00,
     'owner':               hmod.User.objects.get(username='GoveByDaPound'),
     'photo_id':            2,
     'price_per_day':       200.99}
]:

    ra = hmod.Rentable_Article()
    for k, v in data.items():
        setattr(ra, k, v)
    ra.save()

print('Rentable Articles initialized')


#           CREATE RENTAL ITEMS           #

for data in [
    {'transaction_id':          hmod.Transaction.objects.get(customer_id=hmod.User.objects.get(username='Kevbo')).id,
     'amount':                  hmod.Rentable_Article.objects.get(name='Colonial Musket').price_per_day*2,
     'rentable_article_id':     hmod.Rentable_Article.objects.get(name='Colonial Musket').id,
     'date_out':                hmod.Transaction.objects.get(customer_id=hmod.User.objects.get(username='Kevbo')).date,
     'date_due':                datetime.date.today() - datetime.timedelta(1),
     'discount_percent':        1.00},
    {'transaction_id':          hmod.Transaction.objects.get(date=datetime.date.today() - datetime.timedelta(4)).id,
     'amount':                  hmod.Rentable_Article.objects.get(serial_number='R4516').price_per_day*1,
     'rentable_article_id':     hmod.Rentable_Article.objects.get(serial_number='R4516').id,
     'date_out':                hmod.Transaction.objects.get(date=datetime.date.today() - datetime.timedelta(4)).date,
     'date_due':                datetime.date.today() - datetime.timedelta(2),
     'discount_percent':        0.25}
]:

    ri = hmod.Rental_Item()
    for k, v in data.items():
        setattr(ri, k, v)
    ri.amount = ri.amount * Decimal((1-ri.discount_percent))
    ri.save()

print('Rental Items initialized')


#           CREATE RENTAL RETURNS           #

for data in [
    {'rental_item':         hmod.Rental_Item.objects.get(transaction_id=hmod.Transaction.objects.get(date=datetime.date.today() - datetime.timedelta(4)).id),
     'date_returned':       datetime.date.today() - datetime.timedelta(1),
     'return_condition':    'It looks like someone lit it on fire.',
     'handled_by':          hmod.Employee.objects.get(username='Reverend')}
]:

    rr = hmod.Rental_Return()
    for k, v in data.items():
        setattr(rr, k, v)
    rr.save()

print('Rental Returns initialized')


#           CREATE FEES           #

delta = hmod.Rental_Return.objects.first().date_returned - hmod.Rental_Item.objects.get(id=hmod.Rental_Return.objects.first().rental_item.id).date_due

for data in [
    {'transaction':     hmod.Transaction.objects.get(date=datetime.date.today()),
     'rental_item':     hmod.Rental_Return.objects.first().rental_item,
     'rental_return':   hmod.Rental_Return.objects.first(),
     'days_late':       delta.days}
]:
    lf = hmod.Late_Fee()
    for k, v in data.items():
        setattr(lf, k, v)
    lf.amount = hmod.Rentable_Article.objects.get(serial_number='R4516').price_per_day*lf.days_late
    lf.save()

for data in [
    {'transaction':     hmod.Transaction.objects.get(date=datetime.date.today()),
     'rental_item':     hmod.Rental_Return.objects.first().rental_item,
     'rental_return':   hmod.Rental_Return.objects.first(),
     'amount':          400.34,
     'description':     'The back seems to have a symbol burned into it. Who knows what it means.'}
]:

    df = hmod.Damage_Fee()
    for k, v in data.items():
        setattr(df, k, v)
    df.save()

print('Fees initialized')
