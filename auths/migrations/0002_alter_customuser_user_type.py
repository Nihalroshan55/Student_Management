# Generated by Django 4.2.7 on 2023-11-30 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(blank=True, choices=[('teacher', 'Teacher'), ('student', 'Student')], max_length=20),
        ),
    ]