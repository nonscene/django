from rest_framework import serializers
from .models import *



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['color_name', 'id']

class PeopleSerializer(serializers.ModelSerializer):
    Color = ColorSerializer()
    country = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1

    def get_country(self, obj):
        if obj.Color:  # Use the correct attribute name 'Color'
            color_obj = Color.objects.get(id=obj.Color.id)
            return {'color_name': color_obj.color_name, 'hex_code': '#000'}
        else:
            return {'color_name': 'Default Color', 'hex_code': '#000'}

    def validate(self, data):
        special_Character = "!@#$%^&*()_+-<>/?,="
        if any(c in special_Character for c in data['name']):
            raise serializers.ValidationError('name can not contain special character')
        
        if data['age'] > 18:
            raise serializers.ValidationError('age should be greater than 18')
        
        return data