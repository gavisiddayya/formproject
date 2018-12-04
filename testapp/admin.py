from django.contrib import admin
from testapp.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['Name','dob','age']
admin.site.register(Customer,CustomerAdmin)
