# Generated by Django 3.2.4 on 2021-08-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_App', '0002_alter_student_college_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
