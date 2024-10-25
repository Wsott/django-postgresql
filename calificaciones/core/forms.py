from django import forms


class NuevaResenaForm(forms.Form):
    titulo = forms.CharField(label='Titulo para su reseña', max_length=32,
                             widget=forms.TextInput(attrs={
                                 'class': 'w3-input'
                             }))
    comentario = forms.CharField(label='¿Que opina del producto?', max_length=256,
                                 widget=forms.Textarea(attrs={
                                     'class': 'w3-input'
                                 }))
    puntuacion = forms.ChoiceField(label='Le doy...',
                                   choices=[
                                       (1, '⭐ Muy decepcionante...'),
                                       (2, '⭐⭐ Podria ser mejor'),
                                       (3, '⭐⭐⭐ Aceptable pero no sobresale'),
                                       (4, '⭐⭐⭐⭐ Muy bueno, pero con pequeños detalles'),
                                       (5, '⭐⭐⭐⭐⭐ Excelente! Cumple todas mis expectativas')
                                   ],
                                   widget=forms.Select(attrs={
                                       'class': 'w3-input'
                                   }))


class SignInForm(forms.Form):
    nombre = forms.CharField(label="Nombre de usuario", max_length=32,
                             widget=forms.TextInput(attrs={
                                 'class': 'w3-input'
                             }))
    contrasenna = forms.CharField(label="Contraseña", min_length=8, max_length=24,
                                  widget=forms.PasswordInput(attrs={
                                      'class': 'w3-input'
                                  }))
    repetir_contrasenna = forms.CharField(label="Repita la contraseña", min_length=8, max_length=24,
                                          widget=forms.PasswordInput(attrs={
                                              'class': 'w3-input'
                                          }))

    email = forms.EmailField(label='Ingrese su email',
                             widget=forms.EmailInput(attrs={
                                 'class': 'w3-input'
                             }))

    def clean(self):
        datos = super().clean()

        if datos.get('contrasenna') != datos.get('repetir_contrasenna'):
            raise forms.ValidationError('Las contraseñas no coinciden')

        if ' ' in datos.get('contrasenna'):
            raise forms.ValidationError('La contraseña no puede contener espacios')

        if ' ' in datos.get('nombre'):
            raise forms.ValidationError('El nombre de usuario no puede contener espacios')

        return datos


class LogInForm(forms.Form):
    nombre = forms.CharField(label="Nombre de usuario", max_length=32,
                             widget=forms.TextInput(attrs={
                                 'class': 'w3-input'
                             }))
    contrasenna = forms.CharField(label="Contraseña", min_length=8, max_length=24,
                                  widget=forms.PasswordInput(attrs={
                                      'class': 'w3-input'
                                  }))

    def clean(self):
        datos = super().clean()

        if ' ' in datos.get('contrasenna'):
            raise forms.ValidationError('La contraseña no puede contener espacios')

        if ' ' in datos.get('nombre'):
            raise forms.ValidationError('El nombre de usuario no puede contener espacios')

        return datos
