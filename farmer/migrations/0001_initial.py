# Generated by Django 2.2.16 on 2020-09-22 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farm', '0001_initial'),
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=200)),
                ('contact_person', models.CharField(max_length=100)),
                ('contact_person_email', models.EmailField(max_length=254, null=True)),
                ('contact_person_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FarmerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('nin', models.CharField(max_length=50, verbose_name='National Identity Number (NIN)')),
                ('date_of_birth', models.DateField()),
                ('level_of_education', models.CharField(max_length=100)),
                ('marital_status', models.CharField(choices=[(None, '--please select--'), ('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], max_length=15)),
                ('phone_1', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number 1')),
                ('phone_2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone number 2')),
                ('number_of_dependants', models.PositiveIntegerField()),
                ('credit_access', models.BooleanField(choices=[(None, '--please select--'), (True, 'Yes'), (False, 'No')], verbose_name='Have access to credit ?.')),
                ('experience', models.FloatField(verbose_name='Experience in years')),
                ('size_of_land', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Size of land in acres')),
                ('type_of_land', models.CharField(choices=[(None, '---please select---'), ('rented', 'Rented'), ('owned', 'Owned')], max_length=20)),
                ('production_scale', models.CharField(choices=[(None, '---please select---'), ('subsistence', 'subsistence'), ('commercial', 'commercial')], max_length=20)),
                ('general_remarks', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[(None, '--please select--'), ('active', 'Active'), ('in_active', 'In-Active'), ('rejected', 'Rejected')], default='in_active', max_length=20)),
                ('approved_date', models.DateTimeField(blank=True, null=True)),
                ('approver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='unffe_agent', to=settings.AUTH_USER_MODEL)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.County')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.District')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='farmer.Group')),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Parish')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Region')),
                ('sector', models.ManyToManyField(related_name='farmer_sectors', to='farm.Sector')),
                ('sub_county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.SubCounty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to=settings.AUTH_USER_MODEL)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Village')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
