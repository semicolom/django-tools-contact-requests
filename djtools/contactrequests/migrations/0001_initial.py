# Generated by Django 2.2.1 on 2019-05-03 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado')),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone_number', models.CharField(max_length=255, verbose_name='phone number')),
                ('message', models.TextField(verbose_name='message')),
                ('contacted', models.BooleanField(default=False, verbose_name='contacted')),
            ],
            options={
                'verbose_name': 'Contact request',
                'verbose_name_plural': 'Contact requests',
            },
        ),
    ]