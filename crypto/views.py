from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from crypto.forms import ConvertForm, XORForm
from crypto.models import ConvertBinary
from crypto.crypto import *

# Create your views here.

class CryptoView(TemplateView):
    template_name = 'crypto.html'

class CryptoQ1(TemplateView):
    template_name = 'cryptoq1.html'

    def get(self, request, *args, **kwargs):
        form = ConvertForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = ConvertForm(request.POST)

        if form.is_valid():
            hex_string = form.cleaned_data['hex_input']
            
            byte_string = bytes.fromhex(hex_string)
            result = b64_encode(byte_string)
            # return redirect('cryptoq1')

        
            form = ConvertForm()

        args = {'form' : form, 'result' : result}

        return render(request, self.template_name, args)


class CryptoQ2(TemplateView):
    template_name = 'cryptoq2.html'

    def get(self, request, *args, **kwargs):
        form = XORForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = XORForm(request.POST)

        if form.is_valid():
            hex_string = form.cleaned_data['hex_input']
            hex_string2 = form.cleaned_data['hex_input2']
            
            
            result = xor_byte_string(hex_string, hex_string2)
            # return redirect('cryptoq1')

        
            form = XORForm()

        args = {'form' : form, 'result' : result}

        return render(request, self.template_name, args)