from django import forms
from karamchand.models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'entity',
            'address1',
            'address2',
            'city',
            'zip',
            'state',
            'country',
            'website',
            'seeker_email'
        ]