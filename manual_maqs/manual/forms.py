from django import forms

class ManualForm(forms.Form):
    maquina_pesquisa = forms.CharField(label="Máquia", max_length=150, placeholder="Pesquisa")
