from rest_framework import serializers
from karamchand.models import Case


class CaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = (
            'entity',
            'address1',
            'address2',
            'city',
            'zip',
            'state',
            'country',
            'website',
            'seeker_email'
        )
