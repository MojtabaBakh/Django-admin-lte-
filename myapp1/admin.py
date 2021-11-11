from django.contrib import admin
from .models import Data_list

# custome display for Data_list

class Dataadmin(admin.ModelAdmin):
    list_display=("name" , "family" , "mobile" , "code")

admin.site.register(Data_list , Dataadmin)