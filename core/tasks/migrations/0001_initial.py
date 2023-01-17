# Generated by Django 4.1.3 on 2022-12-06 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='título')),
                ('status', models.CharField(choices=[(1, 'To-do'), (2, 'Doing'), (3, 'Done')], max_length=1, verbose_name='status')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='início')),
                ('end_date', models.DateTimeField(auto_now=True, verbose_name='fim')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]