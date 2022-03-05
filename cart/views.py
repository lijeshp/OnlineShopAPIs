from queue import Empty
from django.shortcuts import render
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.reverse import reverse
from app.models import ProductFree
from cart.serializer import CartListSerializer, ItemsfreeSerializer
from .models import Cartlist,ItemsFree
from rest_framework.response import Response

# Create your views here.
def c_id(request):
    ct_id = request.session.session_key
    
    if not ct_id:
        ct_id = request.session.create()
    return ct_id

class CartDetailsView(APIView):
    

    def get(self,request,tot=0,count=0,ct_items=None,*args,**kwargs):
        try:
            ct = Cartlist.objects.get(cart_id=c_id(request))
            ct_items = ItemsFree.objects.filter(cart_id=ct, Active=True)
            for i in ct_items:
                tot += (i.productF.price) * (i.quantF)
                count+=i.quantF
        except ObjectDoesNotExist:
            pass
      
        serializer_one = ItemsfreeSerializer(ct_items,many=True)
        
        return Response({'ct_items':serializer_one.data,'tot':tot,'count':count})

class AddCartView(APIView):
    
    def get(self,request,ProductFree_id,*args,**kwargs):
        prod = get_object_or_404(ProductFree,id=ProductFree_id)
        try:
            ct = Cartlist.objects.get(cart_id=c_id(request))
        except Cartlist.DoesNotExist:
            ct = Cartlist.objects.create(cart_id=c_id(request))
            ct.save()
        try:
            c_items=ItemsFree.objects.get(productF=prod,cart=ct)

            if c_items.quantF < c_items.productF.stock:
                c_items.quantF+=1
                c_items.save()
        except ItemsFree.DoesNotExist:
            c_items=ItemsFree.objects.create(productF=prod,quantF=1,cart=ct)
            c_items.save()
        # serializer_ = ItemsfreeSerializer(c_items)
        # serializer__ = CartListSerializer(ct)
        return redirect('/api/cart-details')
       
    
class MinusCartView(APIView):

    def get(self,request,ProductFree_id,*args,**kwargs):
        ct = Cartlist.objects.get(cart_id=c_id(request))
        prdt = get_object_or_404(ProductFree, id=ProductFree_id)
        c_items = ItemsFree.objects.get(productF= prdt,cart=ct)
       
        if c_items.quantF > 1:
            c_items.quantF-=1
            c_items.save()
        else:
            c_items.delete()
        
        return redirect('/api/cart-details')

class DeleteCartView(APIView):

    def get(self,request,ProductFree_id,*args,**kwargs):

        ct = Cartlist.objects.get(cart_id=c_id(request))
        prdt = get_object_or_404(ProductFree, id=ProductFree_id)
        c_items =ItemsFree.objects.get(productF=prdt,cart=ct)
        c_items.delete()
        return redirect('/api/cart-details')
            