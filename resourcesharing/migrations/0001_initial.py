# Generated by Django 2.2.16 on 2020-09-08 20:45

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmer', '0003_auto_20200908_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=200)),
                ('contacts', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('resource_category', models.CharField(choices=[(None, '--please select--'), ('storage', 'Storage'), ('machinery', 'Machinery'), ('land', 'Land'), ('transportation', 'Transportation')], max_length=25)),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('lon', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('termsandconditions', models.TextField(max_length=400)),
                ('resource_status', models.CharField(choices=[(None, '---please select---'), ('available', 'Available'), ('not available', 'Not Available')], max_length=20)),
                ('availability_date_and_time', models.DateTimeField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.FarmerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceSharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_taken', models.DateTimeField()),
                ('expected_return_date', models.DateTimeField()),
                ('taken_by', models.CharField(max_length=100)),
                ('phone_1', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='contact phone of person who took the resource')),
                ('phone_2', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='contact phone of person who took the resource')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesharing.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_needed', models.DateTimeField(blank=True)),
                ('payment_mode', models.CharField(blank=True, choices=[(None, '--please select--'), ('cash', 'Cash'), ('bank', 'Bank Transfer'), ('cheque', 'Cheque'), ('credit_card', 'Credit/Debit Card'), ('others', 'Others')], max_length=25, null=True)),
                ('payment_method', models.CharField(blank=True, choices=[('full payment', 'Full Payment'), ('installments', 'Installments')], max_length=25, null=True)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.FarmerProfile')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesharing.Resource')),
            ],
        ),
    ]
