from collections import UserList
import email
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth.models import User


class CasaFormulario(forms.Form):

      numero= forms.IntegerField()
      categoria= forms.CharField()     
      domicilio= forms.CharField()       
      tipo= forms.CharField()        
      fecha_disponible= forms.DateField()  
      detalle= forms.CharField()

class FichaFormulario(forms.Form):
      obra= forms.CharField()
      ubicacion= forms.CharField()    
      superficie= forms.IntegerField()    
      construccion= forms.DateField()  
      plazos= forms.CharField()

class ClientesFormulario(forms.Form):
     apellido_y_nombre= forms.CharField()
     referencia= forms.CharField()
     telefono= forms.IntegerField()
     domicilio_legal= forms.CharField()


class UserRegisterForm(UserCreationForm):
      email = forms.EmailField()
      pasword1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
      pasword2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
      
      last_name = forms.CharField()
      first_name = forms.CharField()

      class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
            help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
      email = forms.EmailField(label="Modificar E-mail")
      password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
      password2 = forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)
      

      class Meta:
            model=User
            fields=[ 'email','password1','password2']
            help_texts = {k:"" for k in fields}