from django.contrib import admin
from django.contrib.auth.models import Permission, Group
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.html import mark_safe
from .models import User, UserType, Train, Routes, Booking, Tag, Comment, Ticket, Category
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BookingappAdminSite(admin.AdminSite):
    site_header = "HỆ THỐNG QUẢN LÝ ĐẶT VÉ XE KHÁCH"

    def get_urls(self):
        return [
                   path('train_stats/', self.train_stats)
               ] + super().get_urls()

    def train_stats(self, request):

        count = Train.objects.count()
        stats = Train.objects.annotate(train_count=Count('route_train')).values('id', 'starting_date', 'train_count')
        return TemplateResponse(request, 'admin/train_stats.html', {
            'count': count,
            'stats': stats
        })


admin_site = BookingappAdminSite('myapp')


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_filter = ['name']
    list_display = ['id', 'name']


class UserAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_filter = ['name']
    list_display = ['id', 'name', 'user_type']
    readonly_fields = ['image_view']

    def image_view(self, User):
        if User:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'
                    .format(url=User.image.name)
            )



class TrainInLine(admin.StackedInline):
    model = Train
    fk_name = 'router'


class TrainTagInLine(admin.StackedInline):
    model = Train.tags.through


class RoutesAdmin(admin.ModelAdmin):
    search_fields = ['starting_point', 'ending_point']
    list_filter = ['starting_point', 'ending_point']
    list_display = ['id', 'starting_point', 'ending_point', 'distance']
    inlines = [TrainInLine]


class TrainAdmin(admin.ModelAdmin):
    search_fields = ['starting_date', 'ending_date']
    list_filter = ['starting_date', 'ending_date']
    list_display = ['id', 'starting_date', 'ending_date']
    inlines = [TrainTagInLine]


class TicketsAdmin(admin.ModelAdmin):
    search_fields = ['id', 'price']
    list_filter = ['price', 'point']
    list_display = ['id', 'price', 'point']


class BookingAdmin(admin.ModelAdmin):
    search_fields = ['ticket__price', 'number', 'train__date', 'routes_point']
    list_filter = ['date', 'number', 'pay']
    list_display = ['id', 'number', 'ticket', 'pay']
    readonly_fields = ['total']

    def total(self, Booking):
        if Booking:
            return Booking.ticket.price * Booking.number


class CommentForm(forms.BaseForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentAdmin(admin.ModelAdmin):
    forms = CommentForm

    search_fields = ['name', 'content', 'created_date', 'train']
    list_filter = ['name', 'content', 'created_date', 'train']
    list_display = ['name', 'content', 'created_date', 'train']



# # Register your models here.i
admin_site.register(Group)
admin_site.register(Permission)
admin_site.register(Category, CategoryAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(UserType)
admin_site.register(Train, TrainAdmin)
admin_site.register(Routes, RoutesAdmin)
admin_site.register(Ticket, TicketsAdmin)
admin_site.register(Booking, BookingAdmin)
admin_site.register(Comment, CommentAdmin)
admin_site.register(Tag)
