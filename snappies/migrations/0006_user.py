# Generated by Django 4.2.7 on 2023-12-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snappies', '0005_rename_commande_id_commande_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]
