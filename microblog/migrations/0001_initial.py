# Generated by Django 4.0.4 on 2022-05-03 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import plattuit.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MicroBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='vacío', max_length=50, verbose_name='título')),
                ('body', models.CharField(max_length=200, verbose_name='cuerpo')),
                ('creation_time', models.DateTimeField(default=plattuit.utils.time_zone, verbose_name='fecha de cración')),
                ('update_time', models.DateTimeField(default=plattuit.utils.time_zone, verbose_name='fecha de actualización')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'db_table': 'blog',
            },
        ),
    ]