# Generated by Django 4.1.4 on 2024-03-03 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0004_books_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='image',
            new_name='profile_pic',
        ),
    ]
