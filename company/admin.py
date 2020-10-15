from django.contrib import admin
from .models import Company, General, Code, Type, Contact, Notes

# Register your models here.
admin.site.register(Company)
admin.site.register(General)
admin.site.register(Code)
admin.site.register(Type)
admin.site.register(Contact)
admin.site.register(Notes)
