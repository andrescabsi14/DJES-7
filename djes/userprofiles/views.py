from django.shortcuts import render
from django.contrib.auth import login

from .forms import UserCreationEmailForm, EmailAuthenticationForm

#SignUp View.
def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()

		#Pend loguear después de crear el usuario
		#Pend redireccionar al home


	return render(request, 'signup.html', {'form': form})

#Login View. Never call a function login, logout, authenticate etc.
def signin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		login(request, form.get_user())
		#Pend Redireccionar al home


	return render(request, 'signin.html', {'form': form})