# Generated by Django 2.2.5 on 2019-11-17 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num_reviews',
            field=models.PositiveIntegerField(default=0),
        ),
    ]