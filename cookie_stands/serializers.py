from rest_framework import serializers
from .models import CookieStands


class CookieStandserializer(serializers.ModelSerializer):
    class Meta:
        model = CookieStands
        fields = "__all__"
        ## gets all fields
