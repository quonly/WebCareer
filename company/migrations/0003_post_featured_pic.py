# Generated by Django 4.1.4 on 2023-01-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_productdemo_alter_post_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_pic',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
    ]