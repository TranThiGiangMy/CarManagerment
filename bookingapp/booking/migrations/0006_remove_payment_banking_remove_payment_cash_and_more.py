# Generated by Django 4.0.4 on 2022-05-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_comment_active_tickets_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='banking',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='cash',
        ),
        migrations.AddField(
            model_name='payment',
            name='pay',
            field=models.CharField(choices=[('CA', 'Cash'), ('MM', 'Banking MoMo'), ('ZP', 'Zalo Pay')], max_length=2, null=True),
        ),
    ]