# Generated by Django 4.2.7 on 2023-12-04 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snappies', '0002_alter_commande_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='commande_id',
        ),
        migrations.AlterField(
            model_name='commande',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commande',
            name='value',
            field=models.CharField(max_length=100),
        ),
    ]
