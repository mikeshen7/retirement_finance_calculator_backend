from rest_framework import serializers
from .models import Tax_Bracket


class TaxBracketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax_Bracket
        fields = "__all__"
