from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('productListing/', views.productListing.as_view(), name="productlisting"), #<int:productCategoryID>
]
