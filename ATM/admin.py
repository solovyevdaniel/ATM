from django.contrib import admin
from ATM.models import CustomUser, CustonAdmin


admin.site.register(CustomUser, CustonAdmin)
