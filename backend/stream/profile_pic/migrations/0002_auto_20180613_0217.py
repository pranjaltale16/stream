# Generated by Django 2.0.3 on 2018-06-13 02:17

from django.db import migrations, models
import profile_pic.models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_pic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='Your_DJ_name',
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=profile_pic.models.user_path),
        ),
    ]
