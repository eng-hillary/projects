# Generated by Django 2.2.16 on 2020-09-08 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
        ('farm', '0002_auto_20200908_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='farm.Enterprise')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('business_location', models.CharField(max_length=50, null=True)),
                ('seller_type', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField(max_length=8)),
                ('gender', models.CharField(choices=[(None, '---please select---'), ('female', 'Female'), ('male', 'Male')], max_length=15)),
                ('marital_status', models.CharField(choices=[(None, '--please select--'), ('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], max_length=15)),
                ('enterprise', models.TextField(null=True)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.County')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.District')),
                ('major_products', models.ManyToManyField(related_name='seller', to='openmarket.Product')),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Parish')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Region')),
                ('sub_county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.SubCounty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Village')),
            ],
            options={
                'ordering': ('seller_type',),
            },
        ),
        migrations.CreateModel(
            name='ServiceRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('type',),
            },
        ),
        migrations.CreateModel(
            name='SoilScience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('status', models.BooleanField(default=True)),
                ('operation_mode', models.CharField(max_length=50, null=True)),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('size', models.FloatField(null=True)),
                ('type', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('available_services', models.CharField(blank=True, max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('inventory_status', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50, null=True)),
                ('list_of_service', models.CharField(blank=True, max_length=50)),
                ('service_type', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='serviceprovider', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellerPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=50, null=True)),
                ('price_offer', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery_option', models.CharField(max_length=50)),
                ('payment_options', models.CharField(max_length=50, null=True)),
                ('payment_mode', models.CharField(max_length=50, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openmarket.Seller')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openmarket.Product')),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('status', models.BooleanField(default=True)),
                ('rent', models.CharField(max_length=25, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openmarket.Product')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('status', models.BooleanField(default=True)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical', to='farm.Enterprise')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Logistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50, null=True)),
                ('destination', models.CharField(max_length=50, null=True)),
                ('quantity', models.FloatField(max_length=50, null=True)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('payment_mode', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('inventory_status', models.BooleanField(default=True)),
                ('contact_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openmarket.ContactDetails')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openmarket.ServiceProvider')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openmarket.Product')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='BuyerPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_location', models.CharField(max_length=50)),
                ('quantity', models.FloatField(max_length=50, null=True)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery_options', models.CharField(max_length=50)),
                ('payment_options', models.CharField(max_length=50, null=True)),
                ('payment_mode', models.CharField(max_length=50, null=True)),
                ('Any_other_comment', models.TextField(null=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openmarket.Product')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openmarket.Buyer')),
            ],
        ),
    ]
