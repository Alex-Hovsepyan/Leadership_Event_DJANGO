# Generated by Django 4.2.1 on 2023-05-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_schedules'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchedulesCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=50, verbose_name='Subtitle')),
                ('classname', models.CharField(max_length=30, verbose_name="Classname (Don't Change This)")),
            ],
            options={
                'verbose_name': 'Schedules Categories',
                'verbose_name_plural': 'Schedules Categories',
            },
        ),
    ]
