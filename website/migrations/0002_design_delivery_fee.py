# Generated by Django 4.2 on 2024-01-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='delivery_fee',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
