# Generated by Django 4.2.7 on 2023-12-04 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commande_id', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
