# Generated by Django 4.2.4 on 2023-08-21 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_profile_delete_registration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='course',
            new_name='Courses',
        ),
    ]