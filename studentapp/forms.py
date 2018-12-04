from django import forms

class studentform(forms.Form):

    student_rollno=forms.IntegerField()
    student_name=forms.CharField(max_length=64)
    student_father_name=forms.CharField(max_length=64)
    student_mother_name=forms.CharField(max_length=64)
    student_address=forms.CharField(max_length=64)
    student_email=forms.EmailField()
    student_mobno=forms.CharField()
