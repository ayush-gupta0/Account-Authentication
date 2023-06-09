# Generated by Django 4.1.6 on 2023-02-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Details', '0002_alter_student_info_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='contact',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
