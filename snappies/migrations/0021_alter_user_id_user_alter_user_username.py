# Generated by Django 4.2.7 on 2023-12-05 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snappies', '0020_alter_user_id_user_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_user',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
