
from django.db import models
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser


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
        ordering = ["name"]

    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    name = models.CharField(max_length=50, null=False)
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, related_name='users', null=True)
    sex = models.CharField(max_length=1,choices=SEX, default='M')
    contact = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to='img_avatar/%Y/%m', default=None)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(ModelBase):
    name = models.CharField(max_length=50, unique=True, verbose_name=('starting-point'))

    def __str__(self):
        return self.name

class Routes(models.Model):

    class Meta:
        unique_together = ( 'starting_point', 'ending_point')
        ordering = ['starting_point']

    starting_point = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    ending_point = models.CharField(max_length=100, null=False)
    distance = models.CharField(max_length=100, null=False)
    active = models.BooleanField(default=True)
    note = models.TextField(max_length=50, null=True)

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
    router = models.ForeignKey(Routes, related_name='trains', on_delete=models.SET_NULL, null=True)
    user_train = models.ForeignKey(User, related_name='user_trains', on_delete=models.SET_NULL, null=True)
    empty_seat = models.BooleanField(default=True)
    content = models.TextField(max_length=50, default=True)

    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self.router.starting_point, self.router.ending_point, self.starting_date, self.ending_date)



class Comment(ModelBase):
    name = models.CharField(max_length=50, null=True)
    content = RichTextField()
    train = models.ForeignKey(Train, related_name='comments', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Ticket(ModelBase):
    point = models.ForeignKey(Routes, related_name='point_ticket', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=0, null=False, verbose_name='price')

    def __str__(self):
        return "{0}, {1}".format(self.point, self.price)


class Booking(models.Model):
    PAYMENT = (
        ('CA', 'Cash'),
        ('MM', 'Banking MoMo'),
        ('ZP', 'Zalo Pay')
    )

    ticket = models.ForeignKey(Ticket, related_name='ticket_booking', on_delete=models.SET_NULL, null=True)
    number = models.IntegerField(null=True, verbose_name='number-ticket')
    date = models.ForeignKey(Train, related_name='date_booking', on_delete=models.SET_NULL, null=True)
    note = models.TextField(max_length=50, null=True)
    user_book = models.ForeignKey(User, related_name='user_booking', on_delete=models.SET_NULL, null=True)
    created_date_book = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    pay = models.CharField(max_length=2,choices=PAYMENT, default='CA')



class Tag(models.Model):
    class Meta:
        ordering = ['name']


    name = models.CharField(max_length=58, unique=True)

    def __str__(self):
        return self.name


class ActionBase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'train')
        abstract = True

class Action(ActionBase):
    (LIKE, HAHA, HEART) = range(3)
    ACTIONS = (
        ('LIKE', 'like'),
        ('HAHA', 'haha'),
        ('HEART', 'heart')
    )

    type = models.PositiveSmallIntegerField(choices=ACTIONS, default='LIKE')



class Rating(ActionBase):
    rate = models.PositiveSmallIntegerField(default=0)
