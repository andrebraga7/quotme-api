# Generated by Django 3.2.18 on 2023-05-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_rename_test_quote_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='category',
            field=models.CharField(choices=[('books', 'Books'), ('lyrics', 'Lyrics'), ('statements', 'Statements'), ('originals', 'Originals'), ('out of the box', 'Out of the box')], max_length=32),
        ),
    ]
