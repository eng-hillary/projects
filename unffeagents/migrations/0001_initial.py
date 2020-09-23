# Generated by Django 2.2.16 on 2020-09-22 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openmarket', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_name', models.CharField(max_length=100)),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('market_description', models.TextField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('notice_title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[(None, '--please select--'), ('weather', 'Weather'), ('inputs', 'Inputs'), ('market', 'Market'), ('pests and diseases', 'Pests and Diseases'), ('policies', 'Policies')], max_length=50)),
                ('display_up_to', models.DateTimeField()),
                ('description', models.TextField(max_length=300)),
                ('upload', models.FileField(null=True, upload_to='')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('region', models.ManyToManyField(related_name='target_regions', to='common.Region')),
                ('target_audience', models.ManyToManyField(related_name='target_groups', to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MarketPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('unit_of_measure', models.CharField(max_length=100)),
                ('start_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('end_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unffeagents.Market')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openmarket.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='unffeagent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AgentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('specific_role', models.CharField(choices=[(None, '--please select--'), ('account manager', 'Account Manager'), ('market manager', 'Market Manager'), ('call centre agent', 'Call Centre Agent'), ('notifications and alerts', 'Notifications and Alerts')], max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.District')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
