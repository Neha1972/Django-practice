# Generated by Django 3.1.3 on 2021-12-26 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_room',
            fields=[
                ('class_room_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_room_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_role_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(blank=True, max_length=100, null=True)),
                ('teacher_address', models.CharField(blank=True, max_length=100, null=True)),
                ('teacher_mobile_no', models.BigIntegerField()),
                ('class_room1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_room1', to='clg.class_room')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_role_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(blank=True, max_length=100, null=True)),
                ('student_address', models.CharField(blank=True, max_length=100, null=True)),
                ('student_mobile_no', models.BigIntegerField()),
                ('class_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_room', to='clg.class_room')),
            ],
        ),
    ]
