# Generated by Django 4.2.14 on 2024-10-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagevisits',
            name='path',
            field=models.TextField(blank=True, null=True),
        ),
    ]
