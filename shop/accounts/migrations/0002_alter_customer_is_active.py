# Generated by Django 4.0.5 on 2022-06-07 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
