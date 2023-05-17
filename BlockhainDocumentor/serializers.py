from BlockhainDocumentor.models import Document, Adress, Blockchain
from rest_framework import  serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = ["pk", "domain", "path", "fileName"]

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
class BlockchainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blockchain
        fields = ["pk", "adress", "info"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = User
        # Поля, которые мы сериализуем
        fields = "__all__"

#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["pk", "login", "password", "postAdress"]
