# Generated by Django 2.2.1 on 2019-05-13 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='imageUrl',
            new_name='image_url',
        ),
    ]
