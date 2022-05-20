# Generated by Django 4.0.4 on 2022-05-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=8, verbose_name='price'),
        ),
    ]