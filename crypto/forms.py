from django import forms
from crypto.models import ConvertBinary

class ConvertForm(forms.ModelForm):
    

    class Meta():
        model = ConvertBinary
        fields = ('hex_input',)

        # This is how we connect CSS to the forms, the class is what goes inside CSS
        widgets = {
            'hex_input': forms.TextInput(attrs = {'class' : 'textinputclass'}),
            
        }

class XORForm(forms.ModelForm):

    class Meta():
        model = ConvertBinary
        fields = ('hex_input', 'hex_input2')

        widgets = {
            'hex_input': forms.TextInput(attrs = {'class' : 'textinputclass'}),
            'hex_input2': forms.TextInput(attrs = {'class' : 'textinputclass'}),
        }
