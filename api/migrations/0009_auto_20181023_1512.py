# Generated by Django 2.1.2 on 2018-10-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_post_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]