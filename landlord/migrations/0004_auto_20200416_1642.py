# Generated by Django 3.0.4 on 2020-04-16 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0003_owner_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='plotNo',
        ),
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(choices=[('vacant', 'Vacant'), ('booked', 'Booked'), ('occupied', 'Occupied')], max_length=20, null=True),
        ),
    ]
