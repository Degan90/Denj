# Generated by Django 3.2.6 on 2021-08-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denj', '0004_auto_20210810_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='denj',
            name='image',
            field=models.ImageField(default=[], upload_to='images/'),
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(default=[], upload_to='images/'),
        ),
    ]