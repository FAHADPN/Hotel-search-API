# myapp/serializer.py
from rest_framework import serializers

class KayakURLSerializer(serializers.Serializer):
    destination = serializers.CharField()
    check_in_date = serializers.DateField()
    check_out_date = serializers.DateField('DD-MM-YYYY')


class checkoutDetails(serializers.Serializer):
    name = serializers.CharField()
    number = serializers.IntegerField()
    email = serializers.EmailField()
    destination = serializers.CharField()
    check_in_date = serializers.DateField()
    check_out_date = serializers.DateField('DD-MM-YYYY')
# Define other serializers here if needed
