from rest_framework import serializers
from .models import *

class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Good
        exclude=[]