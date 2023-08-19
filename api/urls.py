from django.urls import path
from .views import DetailProduct,for_productAPI


urlpatterns = [
    path('<int:pk>/',DetailProduct.as_view(),name='detail_pr'),
    path('',for_productAPI.as_view(),name='THeproducts'),
]
