# Generated by Django 4.2.19 on 2025-03-25 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='activity_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attraction',
            name='activity_image',
            field=models.ImageField(blank=True, null=True, upload_to='dine_images/'),
        ),
        migrations.AddField(
            model_name='attraction',
            name='activity_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
