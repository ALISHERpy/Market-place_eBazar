from rest_framework import serializers
from products.models import Product


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=( 'id', 'author', 'category', 'title', 'description', 'price', 'address', 'phone_number', 'tg_username', )