# Generated by Django 2.1.2 on 2018-11-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='customer_details',
        ),
    ]
