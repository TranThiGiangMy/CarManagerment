from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.templatetags.rest_framework import data

from .models import Routes, Tag, Train, TicKet, User, Comment, Booking



class RoutesSerializer(ModelSerializer):
    class Meta:
        model = Routes
        fields =['id', 'starting_point', 'ending_point', 'distance']




class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['d', 'name']



class TrainSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Train
        fields = ['id', 'starting_date', 'ending_date','router', 'tags', 'note', 'empty_seat']


class TrainDetailSerializer(TrainSerializer):
    class Meta:
        model = TrainSerializer.Meta.model
        fields = TrainSerializer.Meta.fields + ['content']


        
class UserSerializer(ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, user):
        request = self.context['request']
        name = user.image.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name
        return request.build_absolute_uri(path)


    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'first_name', 'last_name', 'password', 'email', 'sex', 'contact', 'image', 'active']
        extra_kwargs = {'password': {
                'write_only': True
            }
        }

        def create(self, validated_data):
            data = validated_data.copy()

            user = User(**data)
            user.set_password(user.password)
            user.save()
            return user




class TicketSerializer(ModelSerializer):
    class Meta:
        model = TicKet
        fields = ['id', 'created_date', 'price', 'active']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'content', 'created_date', 'up_date']


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'number', 'created_date_book', 'pay']