from django.shortcuts import get_object_or_404, render

from .models import ProductFree, categ
from django.core.paginator import EmptyPage,InvalidPage,Paginator
from django.conf import settings
from django.http import HttpResponse, Http404
from rest_framework.response import Response


def index(request,c_slug=None):
    c_page = None
    prdtF = None
    prdtP = None
    if c_slug != None:
        c_page =get_object_or_404(categ,slug=c_slug)
        prdtF = ProductFree.objects.filter(category=c_page,available=True)
        # prdtP = ProductPaid.objects.filter(category=c_page,available=True)
    else:
        prdtF = ProductFree.objects.all().filter(available = True)
        # prdtP = ProductPaid.objects.all().filter(available=True)
    cat = categ.objects.all()
    return Response({'obj':prdtF,'cat':cat})