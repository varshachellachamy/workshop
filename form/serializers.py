from rest_framework import serializers
from .models import RegForm


class FormSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegForm
        fields = "__all__"
