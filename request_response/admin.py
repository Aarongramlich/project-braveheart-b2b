from django.contrib import admin
from .models import RequestResponse

# Register your models here.

# admin.site.register(ResponseData) #WILL BE USED FOR API/JSON INSERTS "DAY 2"
admin.site.register(RequestResponse)