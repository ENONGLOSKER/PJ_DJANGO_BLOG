# Generated by Django 4.1.2 on 2022-10-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_database_progres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]
