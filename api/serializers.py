from rest_framework import serializers
from .models import Listing
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ["id","code","name","price","created_at"] 