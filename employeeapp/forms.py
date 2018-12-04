from django import forms
from django.core.validators import ValidationError

def validateemail(email):
    a=email.split('@')
    b = ['mytectra.com', 'yahoo.com', 'gmail.com', 'hotmail.com']
    if a[1] not in b:
        raise ValidationError('not allowed')


class employeeform(forms.Form):


    cn = (

        ('','--select option--'),
        ('cn','chennai'),
        ('hyd','hyderabad'),
        ('bng','bangalore'),
        ('mbi','mumbai')

    )
    gn =(
        ('m','Male'),
        ('f','Female')
    )
    is_active=forms.CharField(widget=forms.CheckboxInput)
    is_active2=forms.BooleanField()
    gender=forms.ChoiceField(choices=gn,widget=forms.RadioSelect)
    city=forms.ChoiceField(choices=cn)
    E_number=forms.IntegerField()
    E_name=forms.CharField()
    E_address=forms.CharField()
    E_email=forms.EmailField(
        validators=[validateemail]
    )
    E_salary=forms.FloatField()
    password1=forms.CharField()
    password2=forms.CharField()

    # def clean(self):
    #     form_data=self.cleaned_data
    #     if 'e_name' in form_data:
    #         print(form_data)
    #         if form_data['e_name'].isdigit():
    #             self.errors['e_name']=['invalid username']
    #
    #
    #     if 'e_email' in form_data:
    #         if form_data['e_email'].split('@')[1] != 'mytectra.com':
    #             self.errors['e_email']=['not allowed']
    #
    #     if 'password1' in form_data and 'password2' in form_data:
    #         if form_data['password1'] != form_data['password2']:
    #             self.errors['password2']=['password mis match']
    #     return form_data
