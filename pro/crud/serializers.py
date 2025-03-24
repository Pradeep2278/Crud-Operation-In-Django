from rest_framework import serializers
from .models import pradeep

class pradeepSerializers(serializers.ModelSerializer):
    class Meta:
        model=pradeep
        fields="__all__"