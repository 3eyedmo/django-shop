# Generated by Django 4.0.5 on 2022-06-21 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.PositiveBigIntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='modification time')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='pay', to='orders.order', verbose_name='order')),
            ],
        ),
    ]
