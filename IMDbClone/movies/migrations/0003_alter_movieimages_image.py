# Generated by Django 3.2 on 2021-10-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20211011_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieimages',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
