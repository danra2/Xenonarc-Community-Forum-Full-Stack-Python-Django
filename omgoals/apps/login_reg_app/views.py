from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from .models import User


def index(request):

	if request.method == "POST":

		bound_form = RegisterForm(request.POST)
		registerForm = RegisterForm()
		loginForm = LoginForm()
		context = {"regForm": registerForm,
					"loginForm": loginForm,
					"errors": bound_form.errors}
		# print bound_form.errors
		print bound_form.is_valid()

		if not request.POST['confirm']:
			messages.error(request, 'This field is required', extra_tags='confirm')
		elif not User.userManager.validate_confirm(request.POST['password'], request.POST['confirm']):
			messages.error(request, 'Password does not match', extra_tags='confirm')
		elif bound_form.is_valid():

			return redirect(reverse('home'))

	else:
		registerForm = RegisterForm()
		loginForm = LoginForm()
		context = {"regForm": registerForm,
					"loginForm": loginForm}

	return render(request, 'login_reg_app/index.html', context)

def success(request):
	return render(request, 'login_reg_app/success.html')


def login(request):

	if User.userManager.login(request.POST['email'], request.POST['password']):
		return redirect(reverse('success'))
	#create flash message for errors
	bound_login = LoginForm(request.POST)
	try:
		messages.error(request, bound_login.errors['email'], extra_tags='email_error')
	except:
		pass
	try:
		messages.error(request, bound_login.errors['password'], extra_tags='password_error')
	except:
		pass
	return redirect(reverse('home'))



