# Generated by Django 3.2.9 on 2024-03-03 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='user_email',
        ),
    ]