# Generated by Django 3.1.4 on 2020-12-15 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201215_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photofolder',
            name='photos',
            field=models.ManyToManyField(blank=True, to='home.Photo'),
        ),
    ]