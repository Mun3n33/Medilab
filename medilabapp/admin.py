from django.contrib import admin
from medilabapp.models import Product, Company, Admission, Registration

# Register your models here.
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Admission)
admin.site.register(Registration)
