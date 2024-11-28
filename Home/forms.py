

#  Manually Crreated File

from django import forms
from Home.models import Contact

class Contact_Form (forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 'email', 'subject', 'message',
        ]
        
        # For styling
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-label1', 'placeholder':'Name',}),
            'email' : forms.EmailInput(attrs={'class':'form-label1', 'placeholder':'Email',}),
            'subject' : forms.TextInput(attrs={'class':'form-label1', 'placeholder':'Subject',}),
            'message': forms.Textarea(attrs={'class':'form-label2', 'placeholder':'Your Message Here', 'rows':4,}),
        }
        # For removing label infornt of box
        labels ={
            'name': '',
            'email': '',
            'subject': '',
            'message': '',
        }