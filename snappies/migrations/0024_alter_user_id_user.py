# Generated by Django 4.2.7 on 2023-12-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snappies', '0023_alter_user_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_user',
            field=models.CharField(primary_key=True, serialize=False),
        ),
    ]
