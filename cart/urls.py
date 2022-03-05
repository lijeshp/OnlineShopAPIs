from django.urls import path,include
from . import views

urlpatterns = [

    path('cart-details', views.CartDetailsView.as_view(), name='cart-details'),
    path('add-cart/<int:ProductFree_id>/',views.AddCartView.as_view(),name='addcart'),
    path('minus-cart/<int:ProductFree_id>/',views.MinusCartView.as_view(),name='minuscart'),
    path('delete-cart/<int:ProductFree_id>/',views.DeleteCartView.as_view(),name='deletecart'),
    
]