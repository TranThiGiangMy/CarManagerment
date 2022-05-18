import datetime

from django.db import models

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserType(models.Model):
    user_type_name = models.CharField(max_length=50)
    ordering = ['user_type_name']

    def __str__(self):
        return self.user_type_name



class ModelBase(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateField(auto_now_add=True)
    up_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)



class User(AbstractUser):
    class Meta:
        unique_together = ('name', 'contact')

    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    name = models.CharField(max_length=50, null=False)
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, related_name='users', null=True)
    sex = models.CharField(max_length=1, choices=SEX)
    contact = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to='img_avatar/%Y/%m', default=None)
    ordering = ["name"]

    def __str__(self):
        return self.name


class Comment(ModelBase):
    name = models.CharField(max_length=50, null=True)
    content = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Routes(models.Model):
    objects = None

    class Meta:
        unique_together = ('starting_point', 'ending_point')

    starting_point = models.CharField(max_length=100, null=False)
    ending_point = models.CharField(max_length=100, null=False)
    distance = models.CharField(max_length=100, null=False)
    active = models.BooleanField(default=True)
    note = models.TextField(max_length=50, null=True)
    ordering = ['starting_point']

    def __str__(self):
        return "{0}, {1}".format(self.starting_point, self.ending_point)


class Train(models.Model):
    class Meta:
        unique_together = ('starting_date', 'ending_date')

    starting_date = models.DateTimeField()
    ending_date = models.DateTimeField()
    tags = models.ManyToManyField('Tag', related_name='tags_trains', blank=True)
    active = models.BooleanField(default=True)
    note = models.TextField(max_length=50, null=True)
    route_train = models.ForeignKey(Routes, related_name='route_trains', on_delete=models.SET_NULL, null=True)
    user_train = models.ForeignKey(User, related_name='user_trains', on_delete=models.SET_NULL, null=True)
    empty_seat = models.BooleanField(default=True)

    def __str__(self):
        return "{0}, {1}".format(self.starting_date, self.ending_date)


class TicKet(ModelBase):
    point = models.ForeignKey(Routes, related_name='point_ticket', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, verbose_name='price')

    def __str__(self):
        return "{0}, {1}".format(self.point, self.price)


class Booking(models.Model):
    PAYMENT = (
        ('CA', 'Cash'),
        ('MM', 'Banking MoMo'),
        ('ZP', 'Zalo Pay')
    )

    ticket = models.ForeignKey(TicKet, related_name='ticket_booking', on_delete=models.SET_NULL, null=True)
    number = models.IntegerField(null=True, verbose_name='number-ticket')
    date = models.ForeignKey(Train, related_name='date_booking', on_delete=models.SET_NULL, null=True)
    note = models.TextField(max_length=50, null=True)
    user_book = models.ForeignKey(User, related_name='user_booking', on_delete=models.SET_NULL, null=True)
    created_date_book = models.DateField(auto_now=True)
    pay = models.CharField(max_length=2, choices=PAYMENT, null=True)

    #
    # def __str__(self):
    #     return "{0}, {1}".format(self.point.starting_point, self.point.ending_point)



class Tag(models.Model):
    name = models.CharField(max_length=58, unique=True)
    ordering = ['name']

    def __str__(self):
        return self.name
