# Generated by Django 4.1 on 2022-08-11 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sisul',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('zipcode', models.CharField(max_length=5)),
                ('safety', models.CharField(max_length=4)),
                ('category', models.CharField(max_length=30)),
                ('info', models.CharField(max_length=30)),
            ],
        ),
    ]
