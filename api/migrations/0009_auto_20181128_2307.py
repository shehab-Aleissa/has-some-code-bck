# Generated by Django 2.1.2 on 2018-11-28 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20181128_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='brand_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ClassesOfTheBrand'),
        ),
    ]
