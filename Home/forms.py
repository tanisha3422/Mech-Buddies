from django import forms
from .models import Customer_Support

class customer_support_form(forms.ModelForm):
    class Meta:
        model = Customer_Support
        fields = ( 'Email', 'Comment')
