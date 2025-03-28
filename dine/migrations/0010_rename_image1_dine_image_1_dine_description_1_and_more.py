# Generated by Django 4.2.19 on 2025-03-22 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dine', '0009_dine_image1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dine',
            old_name='image1',
            new_name='image_1',
        ),
        migrations.AddField(
            model_name='dine',
            name='description_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dine',
            name='features_1',
            field=models.TextField(default='No features available', max_length=100),
        ),
        migrations.AddField(
            model_name='dine',
            name='name_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
