from rest_framework.generics import ListAPIView,RetrieveAPIView 
from products.models import Product
from .serialiezer import Productserializer
# hamma product ucuhun api
class for_productAPI(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer
# bitta pruduct uchun API
class DetailProduct(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer
