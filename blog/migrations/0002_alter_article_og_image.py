# Generated by Django 4.1.3 on 2022-12-05 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='og_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
