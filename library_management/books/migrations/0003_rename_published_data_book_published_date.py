# Generated by Django 5.1.7 on 2025-03-23 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='published_data',
            new_name='published_date',
        ),
    ]
