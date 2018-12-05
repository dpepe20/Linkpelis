from django import forms
from .models import *
from django.contrib.auth.models import User



#REGISTER



class register_form(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	email = forms.EmailField(widget=forms.TextInput())
	password_1 = forms.CharField(label='password', widget=forms.PasswordInput(render_value=False))
	password_2 = forms.CharField(label='confirmar_password', widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('NOMBRE DE USUARIO YA REGISTRADO')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('CORREO ELECTRONICO YA EXISTE')

	def clean_password_2(self):
		password_1 = self.cleaned_data['password_1']
		password_2 = self.cleaned_data['password_2']

		if password_1==password_2:
			pass
		else:
			raise forms.validationError('PASSWORD NO COINCIDEN')


class login_form(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre de Usuario'}))

	password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class contacto_form(forms.Form):

	# required=True es para decirle que es obligatorio llenar los cuadros
	correo = forms.EmailField(max_length=100,widget = forms.TextInput,required=True)
	titulo = forms.CharField(max_length=400,widget = forms.TextInput,required=True)
	texto = forms.CharField(max_length=1000,widget = forms.Textarea,required=True)

class agregar_pelicula_form(forms.ModelForm):
	class Meta:
		model = Pelicula
		fields = '__all__'
		widgets= {
		'fecha' : forms.TextInput(attrs={'class' :'datepicker' })
		}

class agregar_filtro_form(forms.ModelForm):
	class Meta:
		model = Filtro
		fields = '__all__'

class agregar_descarga_form(forms.ModelForm):
	class Meta:
		model = Descarga
		fields = '__all__'

class agregar_recomendacion_form(forms.ModelForm):
	class Meta:
		model = Recomendacion
		fields = '__all__'


class agregar_estreno_form(forms.ModelForm):
	class Meta:
		model = Extreno
		fields = '__all__'
		widgets={
		'fecha_estreno' : forms.TextInput(attrs={'class' : 'datepicker'})
		}

class agregar_genero_form(forms.ModelForm):
	class Meta:
		model = Genero
		fields = '__all__'
