# Generated by Django 3.2.5 on 2022-07-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0009_alter_certification_ttl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='ttl',
            field=models.IntegerField(default=1657451312),
        ),
    ]