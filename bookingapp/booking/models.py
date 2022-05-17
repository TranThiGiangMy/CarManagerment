import datetime

from django.db import models

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserType(models.Model):
    user_type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_type_name



class ModelBase(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateField(auto_now_add=True)
    up_date = models.DateField(auto_now=True)




class User(AbstractUser):
    class Meta:
        unique_together = ('name', 'contact')

    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    name = models.CharField(max_length=50, null=False)
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, related_name='users', null=True)
    sex = models.CharField(max_length=1, choices=SEX, default=None)
    contact = models.CharField(max_length=10, blank=True)
    ordering = ["name"]

    def __str__(self):
        return self.name


class Comment(ModelBase):
    content = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return "{0}, {1}".format(self.content, self.content)


class Routes(models.Model):
    objects = None

    class Meta:
        unique_together = ('starting_point', 'ending_point')

    starting_point = models.CharField(max_length=100, null=False)
    ending_point = models.CharField(max_length=100, null=False)
    distance = models.CharField(max_length=100, null=False)
    note = models.TextField(max_length=50, null=True)

    def __str__(self):
        return "{0}, {1}".format(self.starting_point, self.ending_point)


class Train(models.Model):
    class Meta:
        unique_together = ('starting_date', 'ending_date')

    starting_date = models.DateTimeField()
    ending_date = models.DateTimeField()
    tags = models.ManyToManyField('Tag', related_name='tags_trains', blank=True)
    note = models.TextField(max_length=50, null=True)
    route_train = models.ForeignKey(Routes, related_name='route_trains', on_delete=models.SET_NULL, null=True)
    user_train = models.ForeignKey(User, related_name='user_trains', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{0}, {1}".format(self.starting_date, self.ending_date)


class Tickets(ModelBase):
    price = models.CharField(max_length=50)
    user_ticket = models.ForeignKey(User, related_name='user_tickets', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.price


class Booking(models.Model):
    price = models.ForeignKey(Tickets, related_name='price_booking', on_delete=models.SET_NULL, null=True)
    number = models.CharField(max_length=50, null=True)
    point = models.ForeignKey(Routes, related_name='point_booking', on_delete=models.SET_NULL, null=True)
    date = models.ForeignKey(Train, related_name='date_booking', on_delete=models.SET_NULL, null=True)
    note = models.TextField(max_length=50, null=True)
    user_book = models.ForeignKey(User, related_name='user_booking', on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.number


class Payment(models.Model):
    cash = models.CharField(max_length=50, null=False)
    banking = models.CharField(max_length=50, null=False)
    note = models.TextField(max_length=50, null=True)
    booking = models.ForeignKey(Booking,related_name='booking_payment', on_delete=models.SET_NULL, null=True)
    user_pay = models.ForeignKey(User, related_name='user_payment', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{0}, {1}".format(self.cash, self.banking)


class Bill(models.Model):
    total = models.CharField(max_length=50, null=False)
    created_date = models.DateField(auto_now=True)
    note = models.TextField(max_length=50, null=True)
    user_bill = models.ForeignKey(User, related_name='user_bills', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.total)


class Tag(models.Model):
    name = models.CharField(max_length=58, unique=True)

    def __str__(self):
        return self.name
