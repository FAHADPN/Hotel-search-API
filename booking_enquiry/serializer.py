# myapp/serializer.py
from rest_framework import serializers

class KayakURLSerializer(serializers.Serializer):
    destination = serializers.CharField()
    check_in_date = serializers.DateField()
    check_out_date = serializers.DateField()

# Define other serializers here if needed
