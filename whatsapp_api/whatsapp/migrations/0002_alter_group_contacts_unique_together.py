# Generated by Django 5.0.1 on 2024-07-06 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='group_contacts',
            unique_together={('group', 'number', 'email')},
        ),
    ]
