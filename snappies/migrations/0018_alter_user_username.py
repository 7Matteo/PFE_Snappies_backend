# Generated by Django 4.2.7 on 2023-12-05 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snappies', '0017_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
