from django.contrib import admin, messages
from order.models import order, orderDetail

def mark_as_pending(modeladmin,request,queryset):
    queryset.update(order_status='pending')
    messages.warning(request,'select record(s) marked as pending')

def mark_as_in_progress(modeladmin,request,queryset):
    queryset.update(order_status='in_progress')
    messages.info(request,'select record(s) marked as in progress')
    
def mark_as_Cancelled(modeladmin,request,queryset):
    queryset.update(order_status='Cancelled')
    messages.error(request,'select record(s) marked as Cancelled')

def mark_as_Delivered(modeladmin,request,queryset):
    queryset.update(order_status='Delivered')
    messages.success(request,'select record(s) marked as Delivered')

class orderDetailsInLine(admin.TabularInline):
    model=orderDetail
    extra=1

class orderAdmin(admin.ModelAdmin):
    list_display=['user','date_time','order_status','payment_status']
    list_filter=['order_status','payment_status',]
    date_hierarchy='date_time'
    actions=[mark_as_pending,mark_as_in_progress,mark_as_Cancelled,mark_as_Delivered]
    inlines=[orderDetailsInLine,]

admin.site.register(order,orderAdmin)
# admin.site.register(orderDetail)