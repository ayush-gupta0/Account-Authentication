# Generated by Django 4.1.6 on 2023-02-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Details', '0007_political_leaders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='political_leaders',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
