# Generated by Django 4.2.1 on 2023-05-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_contactget_contactpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactget',
            name='img',
            field=models.ImageField(default=1, upload_to='images', verbose_name='Background Image'),
            preserve_default=False,
        ),
    ]
