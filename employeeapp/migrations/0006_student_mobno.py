 # Generated by Django 2.1.2 on 2018-11-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0005_auto_20181117_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mobno',
            field=models.CharField(default=None, max_length=25),
            preserve_default=False,
        ),
    ]
