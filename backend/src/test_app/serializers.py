from rest_framework import serializers

from .models import TestApi


class TestApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestApi
        fields = ('id', 'name', 'description', 'phone_no','is_alive','amount')
        
        
# consider it as model object
# class SimpleTest:
#     def __init__(self, name) -> None:
#         self.name = name

# ** serialisers
# class SimpleTestSerializer(serializers.Serializer):
#     name = serializers.CharField()
    
# ** running serialiser or the view in this case
# def run_data():
#     instance = SimpleTest("Hasan")
#     serializer = SimpleTestSerializer(instance)
#     print(serializer.data)