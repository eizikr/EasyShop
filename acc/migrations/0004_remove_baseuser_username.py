# Generated by Django 3.1.3 on 2020-11-30 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0003_auto_20201130_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='username',
        ),
    ]
