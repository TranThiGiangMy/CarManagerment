# Generated by Django 4.0.4 on 2022-05-20 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_remove_train_route_train_train_router'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='content',
            field=models.TextField(default=True, max_length=50),
        ),
    ]