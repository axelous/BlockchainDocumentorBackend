from django.db import models  # Подключаем работу с моделями
# Подключаем классы для создания пользователей
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime 
import pytz
# Создаем класс менеджера пользователей
# Создаём класс User



class Document(models.Model):
    name = models.CharField(max_length=10000,verbose_name='Название')
    signature = models.BooleanField(verbose_name='Подпись')
    size = models.CharField(max_length=10, verbose_name='Размер')
    status = models.CharField(max_length=16, verbose_name='Размер', default='отправлен в росздрав')
    docFile = models.FileField(default=None, verbose_name='Файл')
    own = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    # date = models.DateTimeField(default=datetime.now(pytz.timezone('Europe/Moscow')))

    class Meta:
        managed = True
        db_table = "documents"
        verbose_name_plural = "Документы"


class Adress(models.Model):
    domain = models.CharField(max_length=10000)
    path = models.CharField(max_length=10000)
    fileName = models.ForeignKey(Document, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "adresses"

class Blockchain(models.Model):
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    info = models.ForeignKey(Document, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "blockchain"

# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#
#     class Meta:
#         managed = True
#         db_table = 'users'



