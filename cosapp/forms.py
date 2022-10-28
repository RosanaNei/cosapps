from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(label = 'nombre de contacto', required= True)
    apellido = forms.CharField(label = 'apellido de contacto', required = True)
    email = forms.EmailField(label = 'email de contacto', required = True)