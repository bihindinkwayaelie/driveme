# Generated by Django 4.1.1 on 2022-11-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]