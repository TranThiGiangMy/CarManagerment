from rest_framework.serializers import ModelSerializer
from .models import Routes, Tag, Train, TicKet, User

class RoutesSerializer(ModelSerializer):
    class Meta:
        model = Routes
        fields =['id', 'starting_point', 'ending_point', 'distance']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TrainSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Train
        fields = ['id', 'starting_date', 'ending_date', 'tags', 'note']
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'sex', 'comtact', 'image']
        extra_kwargs = {'password': {
                'write_only': True
            }
        }

class TicketSerializer(ModelSerializer):
    class Meta:
        model = TicKet
        fields = ['id', 'created_date', 'price']