from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Student


class StudentInputForm(forms.ModelForm):
    # full_name = forms.CharField(max_length=30)
    # entry_date = forms.DateTimeField()
    # email = forms.EmailField(max_length=254)
    # # faculty = forms.ForeignKey('Faculty', on_delete=forms.CASCADE, max_length=1)
    # interests = forms.CharField(max_length=200, widget=forms.Textarea)
    # password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    # # teacher = forms.ForeignKey('Teacher', on_delete=forms.CASCADE)

    class Meta:
        model = Student
        fields = "__all__"
