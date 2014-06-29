from django.contrib import admin
from customers.models import Client

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','schema_name' , 'domain_url', 'description')

admin.site.register(Client, CustomerAdmin)