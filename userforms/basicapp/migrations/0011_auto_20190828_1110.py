# Generated by Django 2.2.4 on 2019-08-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0010_auto_20190828_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
