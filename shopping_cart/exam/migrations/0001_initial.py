# Generated by Django 3.1.3 on 2021-11-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stuid', models.IntegerField(primary_key=True, serialize=False)),
                ('stuname', models.CharField(max_length=50)),
                ('stuadd', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
