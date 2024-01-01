from rest_framework import serializers
from .models import *

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        models = Color
        fields = ['color_name', 'id']

class PeopleSerializer(serializers.ModelSerializer):
    Color = ColorSerializer()
    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1

    def validate(self, data):
        special_Character = "!@#$%^&*()_+-<>/?,="
        if any(c in special_Character for c in data['name']):
            raise serializers.ValidationError('name can not contain special character')
        
        if data['age'] > 18:
            raise serializers.ValidationError('age should be greater than 18')
        
        return data