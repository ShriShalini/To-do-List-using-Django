# Generated by Django 2.2.4 on 2019-08-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0006_auto_20190827_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]