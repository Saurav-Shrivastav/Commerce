# Generated by Django 3.1.4 on 2020-12-25 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20201225_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]