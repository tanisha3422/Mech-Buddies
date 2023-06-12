from django.contrib import admin
from Home.models import SignUp
from Home.models import Customer_Support
from Home.models import Orders
from Home.models import OrderUpdate

admin.site.register(SignUp)
admin.site.register(Customer_Support)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

# Register your models here.
