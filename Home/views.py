from multiprocessing import context
from pstats import Stats
from django.shortcuts import render
from django.views import View
from product.models import productCategory

class index(View):
    def get(self,request):
        navigationProductCategory=productCategory.objects.filter(status=True)
        productCategory = productCategory.objects.filter(status=True)[0:1]
        context={
            'navigationProductCategory':navigationProductCategory,
            'productCategory':productCategory
            
        }
        
        return render(request,'index.html')
        


