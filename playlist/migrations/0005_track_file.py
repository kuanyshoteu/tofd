# Generated by Django 3.2.9 on 2021-12-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0004_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
