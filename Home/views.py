from multiprocessing import context
from pstats import Stats
from django.shortcuts import render
from django.views import View
from product.models import productCategory

class index(View):
    
    def get(self,request):
        navigationProductCategory=productCategory.objects.filter(status=True)
        homeProductCategory = productCategory.objects.filter(status=True).order_by('name')[0:3]
        context={
            'navigationProductCategory':navigationProductCategory,
            'homeProductCategory':homeProductCategory
            
        }
        
        return render(request,'index.html',context)
        


