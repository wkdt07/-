# Generated by Django 4.2.13 on 2024-05-20 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_depoists_user_savings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='depoists',
            new_name='deposits',
        ),
    ]
