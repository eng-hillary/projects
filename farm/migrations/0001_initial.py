# Generated by Django 2.2.16 on 2020-09-22 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('initial_capital', models.DecimalField(decimal_places=2, max_digits=4)),
                ('expected_profit', models.DecimalField(decimal_places=2, max_digits=4)),
                ('start_date', models.DateField()),
                ('animal_seed_density', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of animals/seedling per enterprise in a particular period or time.')),
                ('image', models.ImageField(upload_to='')),
                ('status', models.CharField(choices=[(None, '--please select--'), ('active', 'Active'), ('closed', 'Closed')], max_length=20, verbose_name='Farm Status')),
                ('general_remarks', models.TextField(blank=True, null=True)),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.Enterprise')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[(None, '--please select--'), ('small', 'Small'), ('large', 'Large')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PestAndDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('picture', models.ImageField(upload_to='')),
                ('date_discovered', models.DateField()),
                ('reporting_date', models.DateField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('action_taken', models.TextField(null=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farm_pests_and_diseases', to='farm.Farm')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FinancialRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('transaction_type', models.CharField(choices=[('income', 'Income'), ('expense', 'expense')], max_length=100)),
                ('spent_on', models.CharField(max_length=200)),
                ('transaction_from', models.CharField(max_length=100)),
                ('transaction_to', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('quantity', models.FloatField()),
                ('means_of_payment', models.CharField(choices=[(None, '--please select--'), ('cash', 'Cash'), ('bank', 'Bank Transfer'), ('cheque', 'Cheque'), ('mobilemoney', 'mobilemoney'), ('credit_card', 'credit card'), ('others', 'Others')], max_length=20)),
                ('transaction_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farm_financial_record', to='farm.Farm')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FarmRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('activity', models.CharField(max_length=200)),
                ('activity_type', models.CharField(choices=[('planting', 'Planting'), ('treatment', 'Treatment'), ('weeding', 'Weeding'), ('harvesting', 'Harvesting')], max_length=30)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('taken_by', models.CharField(max_length=100, null=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farm_records', to='farm.Farm')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FarmProduce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('quantity', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
                ('production_date', models.DateField()),
                ('taken_by', models.CharField(blank=True, max_length=100, null=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farm_produces', to='farm.Farm')),
                ('produce', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farm.Produce')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FarmFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='facilities', to='farm.Farm')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
