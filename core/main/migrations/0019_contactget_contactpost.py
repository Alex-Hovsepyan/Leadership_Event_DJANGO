# Generated by Django 4.2.1 on 2023-05-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_pricing_options_alter_pricingcontent_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactGet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('placeholder1', models.CharField(max_length=50, verbose_name='Placeholder 1')),
                ('placeholder2', models.CharField(max_length=50, verbose_name='Placeholder 2')),
                ('placeholder3', models.CharField(max_length=50, verbose_name='Placeholder 3')),
                ('placeholder4', models.CharField(max_length=50, verbose_name='Placeholder 4')),
                ('btn_name', models.CharField(max_length=40, verbose_name='Button Name')),
            ],
            options={
                'verbose_name': 'Contact GET',
                'verbose_name_plural': 'Contact GET',
            },
        ),
        migrations.CreateModel(
            name='ContactPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='User Name')),
                ('user_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=80, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('date', models.DateField(auto_now=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Contact POST',
                'verbose_name_plural': 'Contact POST',
            },
        ),
    ]