from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['number_courses', 'time_study']
