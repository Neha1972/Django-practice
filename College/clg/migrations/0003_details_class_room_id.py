# Generated by Django 3.1.3 on 2021-12-28 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clg', '0002_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='class_room_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='clg.class_room'),
        ),
    ]
