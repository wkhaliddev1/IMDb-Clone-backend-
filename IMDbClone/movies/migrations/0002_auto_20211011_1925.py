# Generated by Django 3.2 on 2021-10-11 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieimages',
            options={'verbose_name': 'MovieTrailer', 'verbose_name_plural': 'MovieTrailers'},
        ),
        migrations.AlterModelOptions(
            name='movietrailers',
            options={'verbose_name': 'MovieImage', 'verbose_name_plural': 'MovieImages'},
        ),
        migrations.RenameField(
            model_name='movieimages',
            old_name='cover_trailer',
            new_name='cover_photo',
        ),
        migrations.RenameField(
            model_name='movieimages',
            old_name='trailer',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='movietrailers',
            old_name='cover_photo',
            new_name='cover_trailer',
        ),
        migrations.RenameField(
            model_name='movietrailers',
            old_name='image',
            new_name='trailer',
        ),
    ]