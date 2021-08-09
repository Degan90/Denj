# Generated by Django 3.2.6 on 2021-08-02 14:11

from django.conf import settings
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.spatial


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('discoverer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Denj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('location', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('gears', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('discoverer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='denjs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
