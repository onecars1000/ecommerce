from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese la contraseña',
        'class': 'form-control'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirma la contraseña',
        'class': 'form-control'
    })) 
    
    
    
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password','phone_number']
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Ingrese Nombre'
        self.fields['last_name'].widget.attrs['placeholder']='Ingrese Apellido'
        self.fields['email'].widget.attrs['placeholder']='Ingrese Email'
        self.fields['phone_number'].widget.attrs['placeholder']='Ingrese Teléfono'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
            
            
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password!= confirm_password:
        
            raise forms.ValidationError('Las contraseñas no coinciden')
        