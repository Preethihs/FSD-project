# Generated by Django 5.1.4 on 2025-01-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
