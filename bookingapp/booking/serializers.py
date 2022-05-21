from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.templatetags.rest_framework import data

from .models import Routes, Tag, Train, Ticket, User, Comment, Booking, Action, Rating, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class RoutesSerializer(ModelSerializer):
    class Meta:
        model = Routes
        fields =['id', 'starting_point', 'ending_point', 'distance']




class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


        
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


class TrainSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Train
        fields = ['id', 'starting_date', 'ending_date','router', 'tags', 'note', 'empty_seat', 'user_train']


class TrainDetailSerializer(TrainSerializer):
    class Meta:
        model = TrainSerializer.Meta.model
        fields = TrainSerializer.Meta.fields + ['content']


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'created_date', 'price', 'active']


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'name', 'content', 'created_date', 'up_date', 'train', 'user']


class BookingSerializer(ModelSerializer):

    class Meta:
        model = Booking
        fields = ['id','ticket', 'number', 'created_date_book', 'pay', 'user_book', 'active']


class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ['id', 'type', 'created_date']


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rate', 'created_date']


#
# class AuthBusesDetailSerializer(TrainDetailSerializer):
#     like = SerializerMethodField()
#     rating = SerializerMethodField()
#
#
#     class Meta:
#         model = Train
#         fields = TrainDetailSerializer.Meta.fields + ['like', 'rating']
