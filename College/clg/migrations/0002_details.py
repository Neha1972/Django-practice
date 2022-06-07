# Generated by Django 3.1.3 on 2021-12-28 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clg.student')),
                ('teacher_role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clg.teacher')),
            ],
        ),
    ]
