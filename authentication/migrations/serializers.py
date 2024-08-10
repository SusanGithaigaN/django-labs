from rest_framework import serializers
from models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

# model serializer example
# model serializers have a class Meta, & it expects
def validate(self):
    if len(self.password) < 6:
        raise Exception('password has to be > 6')
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =  User
#         fields = '_all_'