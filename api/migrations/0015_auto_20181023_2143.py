# Generated by Django 2.1.2 on 2018-10-23 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='color',
            new_name='exterior_color',
        ),
        migrations.AddField(
            model_name='post',
            name='interior_color',
            field=models.CharField(blank=True, choices=[('White', 'White'), ('Black', 'Black'), ('Blue', 'Blue'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Red', 'Red'), ('Blue', 'Blue'), ('Pink', 'Pink'), ('Purple', 'Purple'), ('Tan', 'Tan'), ('Brown', 'Brown'), ('Grey', 'Grey')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sunroof',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Normal', 'Normal'), ('Panorama', 'Panorama')], max_length=120, null=True),
        ),
    ]