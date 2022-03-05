from django.urls import path,include
from . import views

urlpatterns = [

    # path('',views.display,name='display'),
    # path('',views.product_display,name='product_display'),
    # path('',views.ProductList.as_view(),name='prdt'),
    path('categories/',views.CategoryListView.as_view(),name='categories'),
    path('products/',views.ProductListView.as_view(),name='products'),
    path('categories/<slug:c_slug>/',views.CategoryDetailsView.as_view(),name='prdt_by_cat'),
    path('categories/<slug:c_slug>/<int:ProductFree_id>/',views.ProductDetailsView.as_view(),name='details'),
]
