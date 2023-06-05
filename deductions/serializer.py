from rest_framework import serializers
from .models import Deduction


class DeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deduction
        fields = "__all__"
