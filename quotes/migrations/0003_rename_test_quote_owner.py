# Generated by Django 3.2.18 on 2023-04-25 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_rename_owner_quote_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='test',
            new_name='owner',
        ),
    ]