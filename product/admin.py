from re import search
from django.contrib import admin, messages
#from EdgeShop.product.models import productFeatures
from product.models import productCategory, product, productImage,productFeatures

def make_active(modeladmin, request, queryset):
    queryset.update(status=True)
    messages.success(request, "Selected items are now active")


def make_inactive(modeladmin, request, queryset):
    queryset.update(status=False)
    messages.success(request, "Selected items are now inactive")

class productCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    list_editable = ('status',)
    actions = [make_active, make_inactive]
    # list_display_links = ('id', 'name')
    # list_per_page = 25

class productImageAdmin(admin.TabularInline):
    model=productImage
    extra=1
    classes=('collapse',)

# class productImageAdmin(admin.StackedInline):
#     model=productImage
#     extra=1
#     classes=('collapse',)    

class productFeatureAdmin(admin.TabularInline):
    model=productFeatures
    extra=1

class productAdmin(admin.ModelAdmin):
    list_display=['name','price','product_category','stock','status',]
    list_filter=['product_category','status',]
    search_fields=['name','price',]
    actions=[make_active, make_inactive]
    inlines=[productImageAdmin,productFeatureAdmin] 


admin.site.register(productCategory, productCategoryAdmin)
admin.site.register(product,productAdmin)
