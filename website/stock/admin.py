from django.contrib import admin
from .models import Stockdata
from .models import Tradedata
# Register your models here.

class ListDisplay(admin.ModelAdmin):
    list_display=["firstname","lastname","joined_date",]

admin.site.register(Stockdata,ListDisplay)
admin.site.register(Tradedata)
