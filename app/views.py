
from rest_framework import generics
from django.forms import model_to_dict
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import categ,ProductFree
from . serializer import ProductFreeSerializer,categSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
import json
from app import serializer
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.
class CategoryListView(APIView):

    def get(self,request,format=None,*args,**kwargs):
        queryset =categ.objects.all()
        serializer = categSerializer(queryset, many=True)
        return Response(serializer.data)
    
class CategoryDetailsView(APIView):
    serializer_class = categSerializer
    queryset =categ.objects.all()
    

    def get(self,request,c_slug=None,*args,**kwargs):
        c_page = None
        prdtF= None
        if c_slug != None:
            c_page = get_object_or_404(categ,slug=c_slug)
            prdtF = ProductFree.objects.all().values().filter(category=c_page,available=True)  
        else:
            prdtF = ProductFree.objects.all().values().filter(available = True)  
        cat = categ.objects.filter(slug=c_slug).values()
        
        return Response({'cat':cat,'prdtF':prdtF})




class ProductListView(APIView):

    def get(self,request,format=None,*args,**kwargs):
        queryset =ProductFree.objects.all()
        serializer = ProductFreeSerializer(queryset,many=True)
        return Response(serializer.data)


# def display(request):
#     callapi = requests.get('http://127.0.0.1:8000/api/products/')
#     call_api = requests.get('http://127.0.0.1:8000/api/categories/')
   
   
#     result = call_api.json()
#     results = callapi.json()
#     return render(request,'index.html',{'results':results,'result':result})




class ProductDetailsView(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'product-details.html'
    def get(self,request,format=None,*args,**kwargs):
        queryset =ProductFree.objects.all()
        serializer = ProductFreeSerializer(queryset,many=True)
        return Response(serializer.data)

    def get (self,request,c_slug,ProductFree_id,*args,**kwargs):

        try:
            prductF = ProductFree.objects.filter(category__slug=c_slug,id=ProductFree_id)
            # prductP = ProductPaid.objects.get(category__slug=cc_slug,slug=productP_slug)
        except Exception as e:
            raise e
        serializer = ProductFreeSerializer(prductF,many=True)
        return Response({'prductF':serializer.data})
    
 

# def product_display(request):
#     call_apis = requests.get('http://127.0.0.1:8000/categories/')
#     parameters = {
#         "id" : requests.id
#     }
#     response = requests.get(call_apis,params=parameters)
#     rslt = response.json() 
#     print(rslt)
#     return render(request,'product-details.html',{'rslt':rslt})












        # if c_slug != None:
        #     serializer_class= ProductFreeSerializer
        #     queryset = ProductFree.objects.values()
        #     c_page = get_object_or_404(categ,slug=c_slug)
        #     prdtF = ProductFree.objects.filter(category=c_page,available=True)
        #     # prdtF_dict = model_to_dict(prdtF)
        #     prdtF_ = json.dumps( prdtF)
        # else:
        #     prdtF = ProductFree.objects.all().filter(available = True)
        #     # prdtF_dict = model_to_dict(prdtF)
        #     prdtF_ = json.dumps(  prdtF)
        #     # serializer = categSerializer(categry)
        # cat = categ.objects.all()
        # return Response({'prdtF':prdtF_,'cat':cat})


    


# class CategoryListView(APIView):
#     def get(self,request):
#         categorylist = categ.objects.all()
#         serializer = categSerializer(categorylist, many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = categSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  






# def post (self,request,c_slug,productF_slug,*args,**kwargs):

#         try:
#             prductF = ProductFree.objects.get(category__slug=c_slug,slug=productF_slug)
#             # prductP = ProductPaid.objects.get(category__slug=cc_slug,slug=productP_slug)
#         except Exception as e:
#             raise e
#         return JsonResponse({'prductF':prductF})








