# Generated by Django 4.2 on 2023-07-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyFirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='Email',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
