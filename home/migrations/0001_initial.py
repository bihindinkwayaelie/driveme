# Generated by Django 4.1.1 on 2022-11-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField(null=True)),
                ('phonenumber', models.CharField(max_length=20)),
                ('telephone', models.CharField(default='078', max_length=20)),
                ('address', models.CharField(default='', max_length=30)),
                ('placeofbirth', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=20)),
                ('languages', models.CharField(max_length=50)),
                ('experienceskills', models.CharField(max_length=200)),
                ('workingtime', models.CharField(choices=[('Day', 'Day'), ('Night', 'Night')], max_length=50, null=True)),
                ('idcard', models.FileField(upload_to='IdFolder')),
                ('licensecard', models.FileField(upload_to='LicenseFolder')),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('working', models.BooleanField(default=False, verbose_name='Working')),
                ('created', models.DateTimeField(null=True)),
            ],
        ),
    ]
