from django import forms
from employeeapp.models import Collage

class CollageForm(forms.ModelForm):

    class Meta:
        model=Collage
        # fields=('name','email')
        fields=('email','address','city')
