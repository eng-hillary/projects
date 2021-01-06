# Generated by Django 3.0.4 on 2020-04-17 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0005_auto_20200416_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='approval',
            field=models.CharField(choices=[('approved', 'Approved'), ('unapproved', 'Unapproved')], default='unapproved', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='landlord.Owner'),
        ),
        migrations.AlterField(
            model_name='house',
            name='rooms',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
