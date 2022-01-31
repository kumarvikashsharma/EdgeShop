from django.contrib import admin
from cart.models import cart

class cartAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity',]
    search_fields=['product__name','user__first_name']

admin.site.register(cart,cartAdmin)