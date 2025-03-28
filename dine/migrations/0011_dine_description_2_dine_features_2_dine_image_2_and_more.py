# Generated by Django 4.2.19 on 2025-03-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dine', '0010_rename_image1_dine_image_1_dine_description_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dine',
            name='description_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dine',
            name='features_2',
            field=models.TextField(default='No features available', max_length=100),
        ),
        migrations.AddField(
            model_name='dine',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='dine_images/'),
        ),
        migrations.AddField(
            model_name='dine',
            name='name_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
