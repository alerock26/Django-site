from django import forms

class contact_form(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True)
    email  = forms.CharField(label='Correo', required=True)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea())
