# Generated by Django 4.0.4 on 2022-05-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(default=None, upload_to='img_avatar/%Y/%m'),
        ),
    ]
