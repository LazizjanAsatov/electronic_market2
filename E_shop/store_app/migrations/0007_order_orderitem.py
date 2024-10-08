# Generated by Django 5.0.6 on 2024-08-08 13:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0006_contact_us'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('additional_info', models.TextField()),
                ('amount', models.IntegerField()),
                ('date', models.DateField(default='datetime.date.today')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=123)),
                ('image', models.ImageField(upload_to='Product_images/Order_Img')),
                ('quantity', models.CharField(max_length=123)),
                ('price', models.CharField(max_length=123)),
                ('total', models.CharField(max_length=1203)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.order')),
            ],
        ),
    ]
