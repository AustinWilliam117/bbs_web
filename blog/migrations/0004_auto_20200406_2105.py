# Generated by Django 2.2.11 on 2020-04-06 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_meat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_time']},
        ),
    ]
