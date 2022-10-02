from webbrowser import get
from django import forms
from core.models import Produto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class PerfilEditForm(ModelForm):
    class Meta:
        model = User

        fields = ('first_name', 'last_name', 'email')
        


    
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name' ,'last_name')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user
        

class ProdutoModelForm(forms.ModelForm):

    # usuario = forms.CharField( disabled=True)
    
    class Meta:
        model = Produto
        
        fields = ['postagem','imagem', 'tags','usuario']
       
        # tirei usuario

        