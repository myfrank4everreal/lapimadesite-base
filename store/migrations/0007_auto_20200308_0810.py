# Generated by Django 2.2.8 on 2020-03-08 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200308_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busineszone',
            name='img_url',
            field=models.CharField(default='img', max_length=900),
        ),
        migrations.AlterField(
            model_name='gamezone',
            name='img_url',
            field=models.CharField(default='img', max_length=900),
        ),
        migrations.AlterField(
            model_name='gigzone',
            name='img_url',
            field=models.CharField(default='img', max_length=900),
        ),
        migrations.AlterField(
            model_name='products',
            name='img_url',
            field=models.CharField(default='img', max_length=900),
        ),
    ]
