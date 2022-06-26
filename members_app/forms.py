from django import forms
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Profile

# create login form


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Digite um nome de usuário para você'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nome'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Sobrenome'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme sua senha'
        self.fields['username'].label = 'Digite um nome de usuário para você'
        self.fields['first_name'].label = 'Nome'
        self.fields['last_name'].label = 'Sobrenome'
        self.fields['email'].label = 'E-mail'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme sua senha'
        self.fields['email'].label = 'E-mail'
        self.fields['username'].help_text = 'Requerimento: Até 150 caracteres que tenha letras e @ / . + - _ apenas'
        self.fields['password1'].help_text = '''<ul>  
                                                    <li>Sua senha não deve ser similar a outras informações pessoais fornecidas.</li>  
                                                    <li>Sua senha precisa ter no mínimo 8 caracteres.</li>
                                                     <li>Sua senha não poderá conter apenas números.</li>
                                                </ul>'''
        self.fields['password2'].help_text = 'Digite a mesma senha informada no campo acima.'
        
class MySetPasswordForm(SetPasswordForm):

    def save(self, *args, commit=True, **kwargs):
        user = super().save(*args, commit=False, **kwargs)
        user.is_active = True
        if commit:
            user.save()
        return user
    def __init__(self, *args, **kwargs):
        super(MySetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Nova Senha'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirme a senha'
        self.fields['new_password1'].label = 'Nova Senha'
        self.fields['new_password2'].label = 'Confirme a senha'
        self.fields['new_password1'].help_text = '''<ul>  
                                                    <li>Sua senha não deve ser similar a outras informações pessoais fornecidas.</li>  
                                                    <li>Sua senha precisa ter no mínimo 8 caracteres.</li>
                                                     <li>Sua senha não poderá conter apenas números.</li>
                                                </ul>'''
        self.fields['new_password2'].help_text = 'Digite a mesma senha informada no campo acima.'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = 'E-mail'
        self.fields['username'].label = 'Digite um nome de usuário para você'
        self.fields['username'].help_text = 'Requerimento: Até 150 caracteres que tenha letras e @ / . + - _ apenas'

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','user_authorized']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['type'] = 'file'
        self.fields['image'].label = 'image'
  
class ProfileUpdateForm_edit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm_edit, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['type'] = 'file'
        self.fields['image'].label = 'image'

