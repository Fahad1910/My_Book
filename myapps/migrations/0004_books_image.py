# Generated by Django 4.1.4 on 2024-03-01 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0003_rename_booksmodel_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
