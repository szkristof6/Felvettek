# Generated by Django 3.1.7 on 2021-03-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Felvettekapp', '0004_auto_20210309_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
