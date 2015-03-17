# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import localflavor.us.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')], max_length=20)),
                ('email', models.EmailField(unique=True, verbose_name='email address', max_length=255)),
                ('first_name', models.CharField(null=True, blank=True, max_length=100)),
                ('last_name', models.CharField(null=True, blank=True, max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('security_question', models.TextField(null=True, max_length=60)),
                ('security_answer', models.TextField(null=True, max_length=30)),
                ('requires_reset', models.BooleanField(default=False)),
                ('phone', localflavor.us.models.PhoneNumberField(null=True, max_length=20)),
                ('organization_name', models.TextField(null=True, max_length=100)),
                ('bio_sketch', models.TextField(null=True, max_length=200)),
                ('emergency_contact_relationship', models.TextField(null=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('address1', models.TextField(null=True, max_length=200)),
                ('address2', models.TextField(null=True, max_length=200)),
                ('city', models.TextField(null=True, max_length=30)),
                ('state', localflavor.us.models.USStateField(max_length=2, default='', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')])),
                ('zip_code', localflavor.us.models.USZipCodeField(null=True, blank=True, max_length=10)),
            ],
            options={
                'ordering': ['state', 'city', 'zip_code', 'address1', 'address2'],
                'verbose_name_plural': 'addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('place_number', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(null=True, max_length=30)),
                ('description', models.TextField(null=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clothing_Detail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('size', models.TextField(null=True, max_length=100)),
                ('size_modifier', models.TextField(null=True, max_length=100)),
                ('gender', models.CharField(null=True, max_length=10)),
                ('color', models.CharField(null=True, max_length=10)),
                ('pattern', models.TextField(null=True, max_length=100)),
                ('start_year', models.IntegerField(null=True, max_length=10)),
                ('end_year', models.IntegerField(null=True, max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Damage_Fee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('amount', models.DecimalField(null=True, decimal_places=2, max_digits=10)),
                ('waived', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('date_hired', models.DateTimeField(null=True)),
                ('salary', models.DecimalField(null=True, decimal_places=2, max_digits=10)),
                ('wage', models.DecimalField(null=True, decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('homepage.user',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('map_file_name', models.TextField(max_length=200)),
                ('venue_name', models.TextField(max_length=200)),
                ('address', models.ForeignKey(related_name='+', to='homepage.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expected_Sale_Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Historical_Figure',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('birth_date', models.DateField(null=True)),
                ('birth_place', models.TextField(null=True, blank=True, max_length=200)),
                ('death_date', models.DateField(null=True)),
                ('death_place', models.TextField(null=True, blank=True, max_length=200)),
                ('biographical_note', models.TextField()),
                ('is_fictional', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(null=True, max_length=100)),
                ('description', models.TextField(null=True, max_length=300)),
                ('serial_number', models.TextField(null=True, max_length=100)),
                ('value', models.DecimalField(null=True, decimal_places=2, max_digits=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Late_Fee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('amount', models.DecimalField(null=True, decimal_places=2, max_digits=10)),
                ('waived', models.BooleanField(default=False)),
                ('days_late', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order_Form',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('customer_info', models.TextField(null=True, max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date_taken', models.DateTimeField(null=True)),
                ('place_taken', models.TextField(null=True, max_length=30)),
                ('description', models.TextField(null=True, max_length=200)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Public_Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rental_Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('amount', models.DecimalField(null=True, decimal_places=2, max_digits=10)),
                ('date_out', models.DateTimeField(null=True)),
                ('date_due', models.DateTimeField(null=True)),
                ('discount_percent', models.DecimalField(null=True, decimal_places=2, max_digits=3)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rental_Return',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('return_condition', models.TextField(null=True, max_length=200)),
                ('date_returned', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('type', models.TextField(max_length=40)),
                ('area', models.ForeignKey(to='homepage.Area')),
                ('historical_figure', models.ForeignKey(to='homepage.Historical_Figure')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale_Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('amount', models.DecimalField(null=True, decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('order_form', models.ForeignKey(to='homepage.Order_Form', null=True, related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store_Item',
            fields=[
                ('item_ptr', models.OneToOneField(to='homepage.Item', primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('quantity_on_hand', models.IntegerField(null=True, max_length=10)),
                ('shelf_location', models.TextField(null=True, max_length=100)),
                ('order_file', models.TextField(null=True, max_length=100)),
            ],
            options={
            },
            bases=('homepage.item',),
        ),
        migrations.CreateModel(
            name='Sale_Product',
            fields=[
                ('store_item_ptr', models.OneToOneField(to='homepage.Store_Item', primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('production_time', models.CharField(null=True, max_length=100)),
                ('price', models.DecimalField(null=True, decimal_places=2, max_digits=10)),
                ('manufacturer', models.CharField(null=True, max_length=100)),
            ],
            options={
            },
            bases=('homepage.store_item',),
        ),
        migrations.CreateModel(
            name='Custom_Product',
            fields=[
                ('sale_product_ptr', models.OneToOneField(to='homepage.Sale_Product', primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('required_info', models.TextField(null=True, max_length=300)),
            ],
            options={
            },
            bases=('homepage.sale_product',),
        ),
        migrations.CreateModel(
            name='Rentable_Article',
            fields=[
                ('store_item_ptr', models.OneToOneField(to='homepage.Store_Item', primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('price_per_day', models.DecimalField(null=True, decimal_places=2, max_digits=10)),
                ('condition_new', models.BooleanField(default=False)),
                ('notes', models.TextField(null=True, max_length=300)),
            ],
            options={
            },
            bases=('homepage.store_item',),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateTimeField(null=True)),
                ('phone', models.CharField(null=True, max_length=12)),
                ('date_packed', models.DateTimeField(null=True)),
                ('date_paid', models.DateTimeField(null=True)),
                ('date_shipped', models.DateTimeField(null=True)),
                ('tracking_number', models.TextField(null=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('SSN', localflavor.us.models.USSocialSecurityNumberField(null=True, max_length=11)),
                ('EIN', models.CharField(null=True, max_length=10)),
                ('UTTaxID', models.CharField(null=True, max_length=10)),
                ('sales_tax_return_form_given', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('homepage.user',),
        ),
        migrations.AddField(
            model_name='transaction',
            name='customer',
            field=models.ForeignKey(related_name='orders', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='handled_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='handledby'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_processed_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='paymentprocessedby'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='shipped_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='shippedby'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='ships_to',
            field=models.ForeignKey(to='homepage.Address', blank=True, null=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sale_product',
            name='creator',
            field=models.ForeignKey(null=True, to='homepage.Vendor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sale_item',
            name='product',
            field=models.ForeignKey(related_name='+', to='homepage.Sale_Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sale_item',
            name='transaction',
            field=models.ForeignKey(to='homepage.Transaction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='role',
            name='participant',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rental_return',
            name='handled_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='rentalhandledby'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rental_return',
            name='rental_item',
            field=models.ForeignKey(to='homepage.Rental_Item', null=True, related_name='return_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rental_item',
            name='rentable_article',
            field=models.ForeignKey(to='homepage.Rentable_Article'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rental_item',
            name='transaction',
            field=models.ForeignKey(to='homepage.Transaction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='late_fee',
            name='rental_item',
            field=models.ForeignKey(to='homepage.Rental_Item', null=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='late_fee',
            name='rental_return',
            field=models.ForeignKey(to='homepage.Rental_Return', null=True, related_name='late_fee_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='late_fee',
            name='transaction',
            field=models.ForeignKey(to='homepage.Transaction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(null=True, related_name='+', to='homepage.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='clothing_detail',
            field=models.ForeignKey(to='homepage.Clothing_Detail', null=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ForeignKey(related_name='+', to='homepage.Photograph'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='expected_sale_item',
            name='photo',
            field=models.ForeignKey(to='homepage.Photograph', null=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='public_event',
            field=models.ForeignKey(to='homepage.Public_Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='damage_fee',
            name='rental_item',
            field=models.ForeignKey(to='homepage.Rental_Item', null=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='damage_fee',
            name='rental_return',
            field=models.ForeignKey(to='homepage.Rental_Return', null=True, related_name='damage_fee_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='damage_fee',
            name='transaction',
            field=models.ForeignKey(to='homepage.Transaction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='coordinator',
            field=models.ForeignKey(related_name='coordinates', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='event',
            field=models.ForeignKey(to='homepage.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='homepage.Role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='supervisor',
            field=models.ForeignKey(related_name='supervises', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ForeignKey(to='homepage.Address', blank=True, null=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='emergency_contact',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', blank=True, related_query_name='user', related_name='user_set', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='id_photo',
            field=models.ForeignKey(to='homepage.Photograph', blank=True, null=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(help_text='Specific permissions for this user.', to='auth.Permission', blank=True, related_query_name='user', related_name='user_set', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
