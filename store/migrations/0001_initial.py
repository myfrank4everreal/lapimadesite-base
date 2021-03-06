# Generated by Django 3.0.2 on 2020-01-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=300)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]
