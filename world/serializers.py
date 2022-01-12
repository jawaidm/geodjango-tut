from rest_framework import serializers
from .models import DpawRegion


class DpawRegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DpawRegion
        #fields = '__all__'
        exclude = ('geom', )

