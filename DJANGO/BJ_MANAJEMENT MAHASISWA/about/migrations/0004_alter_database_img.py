# Generated by Django 4.1.2 on 2022-10-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_database_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='img',
            field=models.ImageField(upload_to='img'),
        ),
    ]