from rest_framework import serializers
from . models import employees

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=employees
        fields= '__all__' # ?('firstnma','latsnam')
        # read_only_fields=
