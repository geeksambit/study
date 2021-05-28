from rest_framework import serializers
from materials.models import Class


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'
        read_only_fields = []
