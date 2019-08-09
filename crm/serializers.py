from rest_framework import serializers
from .models import Customer, Service, Product


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'cust_name', 'organization', 'role', 'email', 'bldgroom', 'address', 'account_number',
                  'city', 'state', 'zipcode', 'phone_number')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('pk', 'cust_name', 'service_category', 'description', 'location', 'setup_time', 'cleanup_time',
                  'service_charge', 'created_date', 'updated_date')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'cust_name', 'product', 'p_description', 'quantity', 'pickup_time', 'charge',
                  'created_date', 'updated_date')
