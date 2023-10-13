from django import forms
    
class PrendaFormulario(forms.Form):
    tipo = forms.CharField()
    costo = forms.IntegerField()
    genero = forms.CharField()


