# Generated by Django 4.0.3 on 2022-03-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_profile_licenses_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Image',
            field=models.ImageField(default='/profile_default.jpg', upload_to='', verbose_name='Profile Picture'),
        ),
    ]