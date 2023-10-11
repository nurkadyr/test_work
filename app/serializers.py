from rest_framework import serializers


class FormulaSerializer(serializers.Serializer):
    formula = serializers.CharField(required=True)
