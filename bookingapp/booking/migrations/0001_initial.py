# Generated by Django 4.0.4 on 2022-05-14 15:35

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(upload_to='uploads/%Y/%m')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, null=True)),
                ('note', models.TextField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_point', models.CharField(max_length=100)),
                ('ending_point', models.CharField(max_length=100)),
                ('distance', models.CharField(max_length=100)),
                ('note', models.TextField(max_length=50, null=True)),
            ],
            options={
                'unique_together': {('starting_point', 'ending_point')},
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=58, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type_name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(default=None, upload_to='img_avata/%Y/%m')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('upp_date', models.DateField(auto_now=True)),
                ('contact', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('routes', models.ManyToManyField(blank=True, related_name='routes_user', to='booking.routes')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.DateTimeField()),
                ('ending_date', models.DateTimeField()),
                ('note', models.TextField(max_length=50, null=True)),
                ('route_train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='route_trains', to='booking.routes')),
                ('tags', models.ManyToManyField(blank=True, related_name='tags_trains', to='booking.tag')),
                ('user_train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_trains', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('starting_date', 'ending_date')},
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('upp_date', models.DateField(auto_now=True)),
                ('user_ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_tickets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.CharField(max_length=50)),
                ('banking', models.CharField(max_length=50)),
                ('note', models.TextField(max_length=50, null=True)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_payment', to='booking.booking')),
                ('user_pay', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_payment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('upded_date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='date_booking', to='booking.train'),
        ),
        migrations.AddField(
            model_name='booking',
            name='point',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='point_booking', to='booking.routes'),
        ),
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='price_booking', to='booking.tickets'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_booking', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=50)),
                ('created_date', models.DateField(auto_now=True)),
                ('note', models.TextField(max_length=50, null=True)),
                ('user_bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_bills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='booking.usertype'),
        ),
    ]
