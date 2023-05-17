import grpc
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework_jwt.utils import jwt_decode_handler
import text_pb2_grpc
import text_pb2
from .models import Document
from rest_framework_simplejwt.authentication import JWTAuthentication
from BlockhainDocumentor.serializers import DocumentSerializer, AdressSerializer, BlockchainSerializer, UserSerializer
from BlockhainDocumentor.models import Document, Adress, Blockchain
from django.conf import settings
from django.contrib.auth.models import User
import redis

import io, hashlib, hmac

from .web3_py_simple_storage.deploy import deploy

from web3 import Web3

# In the video, we forget to install_solc
# from solcx import compile_standard
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware

session_storage = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    def get_queryset(self):
        queryset = Document.objects.all()
        if self.request.method == 'GET':
            if self.request.headers.get("Authorization"):
                decoded_payload = jwt_decode_handler(self.request.headers.get("Authorization")[7:])
                user_id = decoded_payload.get('user_id')
                if not User.objects.get(id=user_id).is_superuser:
                    queryset = queryset.filter(own=user_id)
            if self.request.query_params.get('q'):
                q = self.request.query_params.get('q')
                queryset = queryset.filter(name__icontains=q)
            if self.request.query_params.get('date'):
                date = self.request.query_params.get('date')
                queryset = queryset.filter(date__icontains=date)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # file = serializer.validated_data["docFile"]
        # print(serializer.validated_data)
        # print(Document.objects.last())
        file = Document.objects.last()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(123)
        # b = r"D:\Code\NEWESTBACKENDBCD\Backend\media"
        # a = os.path.abspath(str(file.docFile)).replace(r"D:\\Code\\NEWESTBACKENDBCD\\Backend\\", b)
        # print(b)
        # print(a)
        hash_md5 = hashlib.md5()
        with open(str(os.path.abspath(str(file.docFile))), "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        print(hash_md5.hexdigest())
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = text_pb2_grpc.TextServiceStub(channel)
            response = stub.sendText1(text_pb2.TextRequest1(text=str(hash_md5.hexdigest())))
        # res = deploy(str(hash_md5.hexdigest()))
        print('Hash file saved succesfully.')
        print(response.text)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id = False
        if request.headers.get("Authorization"):
            decoded_payload = jwt_decode_handler(request.headers.get("Authorization")[7:])
            user_id = decoded_payload.get('user_id')
            print(User.objects.get(id=user_id).is_superuser)
        if user_id:
            if User.objects.get(id=user_id).is_superuser:
                instance.status = request.data.get("status")
                instance.save()
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)

    #def post(self, request, format=None):
    #    request.data['requestjsondata'] = json.dumps(request.data['requestjsondata'])
    #    requestData = DocumentSerializer(data=request.data)
    #    if requestData.is_valid():
    #        SerializerResponse = requestData.save()
    #        request.data['id'] = SerializerResponse.pk
    #    return Response(request.data, status=status.HTTP_201_CREATED)
#
#     def delete(self, request,  *args, **kwargs):
#         object = self.get_object()
#         object.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# #
# @csrf_exempt
# def delete(self, request, pk, *args, **kwargs):
#     object = self.get_object(pk)
#     object.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def post(request):
    print(request.body)
    return HttpResponse('ok')

# class DeleteDocumentViewSet(viewsets.ModelViewSet):
#     queryset = Document.objects.all()
#     def destroy(self, request, *args, **kwargs):

class AdressViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Adress.objects.all()
    serializer_class = AdressSerializer  # Сериализатор для модели
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer  # Сериализатор для модели

class BlockchainViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Blockchain.objects.all()
    serializer_class = BlockchainSerializer  # Сериализатор для модели

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint, который позволяет просматривать и редактировать акции компаний
#     """
#     # queryset всех пользователей для фильтрации по дате последнего изменения
#     queryset = User.objects.all()
#     serializer_class = UserSerializer  # Сериализатор для модели

# class Document(models.Model):
#     name = models.CharField(max_length=10000)
#     type = models.CharField(max_length=50)
#     signature = models.BooleanField()
#     size = models.FloatField()
#     docFile = models.FileField(default=None)
class UserUploadedPicture(APIView):
    parser_classes = (MultiPartParser, )
    def post(self, request, format=None):
        print(request.data)
        data = request.data
        print("\n\n\n")
        Document.objects.create(name = data['name'], size = data['size'], signature = data['signature'], docFile = data['data'], own = data['own'])

        return HttpResponse('ok')

@api_view(['GET', 'POST'])
def getJson(request):
    if request.method == 'POST':
        print(request.data)
        user = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'])
        user.save()
        return HttpResponse("{'status': 'ok'}")
    else:
        return HttpResponse("{'status': 'neok'}")
        
@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def user(request: Request):
    return Response({
        'data': UserSerializer(request.user).data
    })
