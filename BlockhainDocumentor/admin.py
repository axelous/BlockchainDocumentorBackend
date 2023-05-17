from django.contrib import admin
from .models import Document, Blockchain, Adress

# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass

@admin.register(Blockchain)
class BlockchainAdmin(admin.ModelAdmin):
    pass

@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    pass
