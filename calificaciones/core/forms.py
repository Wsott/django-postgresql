from django import forms


class SignInForm(forms.Form):
    nombre = forms.CharField(label="Nombre de usuario", max_length=32)
    contrasenna = forms.CharField(label="Contraseña", min_length=8, max_length=24, widget=forms.PasswordInput())
    repetir_contrasenna = forms.CharField(label="Repita la contraseña", min_length=8, max_length=24,
                                          widget=forms.PasswordInput())

    def clean(self):
        datos = super().clean()

        if datos.get('contrasenna') != datos.get('repetir_contrasenna'):
            raise forms.ValidationError('Las contraseñas no coinciden')

        if ' ' in datos.get('contrasenna'):
            raise forms.ValidationError('La contraseña no puede contener espacios')

        if ' ' in datos.get('nombre'):
            raise forms.ValidationError('El nombre de usuario no puede contener espacios')

        return datos
