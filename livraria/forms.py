from django import forms

from livraria.models import Livro

class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = ('nome','autor','categoria','codigo', 
        'quantidade', 'valor', 'imagem', 'ano', 'descricao')

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Ex: Redes de Computadores'}),
            'autor': forms.SelectMultiple(attrs={ 'class': 'form-control'}),
            'categoria': forms.Select(attrs={ 'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={ 'class': 'form-control',
                                              'placeholder':'Ex:010103'}),
            'quantidade': forms.TextInput(attrs={ 'class': 'form-control'}),
            'valor': forms.TextInput(attrs={ 'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={ 'class': 'form-control'}),
            'ano': forms.TextInput(attrs={ 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={ 'class': 'form-control'}),
        }