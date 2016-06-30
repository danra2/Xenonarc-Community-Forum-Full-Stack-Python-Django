from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
from django.contrib import messages

def index(request):
	return render(request, 'login_reg_app/index.html')

def signin(request):
	if User.userManager.login_val(request.POST['email'], request.POST['password']):
		request.session['id'] = User.userManager.get_id(request.POST['email'],request.POST['password'])
		return redirect(reverse('dash'))
	else:
		messages.error(request, 'Invalid Login', extra_tags='login')
		return redirect(reverse('index'))

def register(request):
	return render(request, 'login_reg_app/register.html')

def validation(request):

	if request.method =='POST':
		valid = True
		if not User.userManager.name_val(request.POST['first_name']):
			messages.error(request, 'Name must be longer than 2 characters, Letters only', extra_tags='first_name')
			valid = False
		if not User.userManager.name_val(request.POST['last_name']):
			messages.error(request, 'Name must be longer than 2 characters, Letters only', extra_tags='last_name')
			valid = False
		if not User.userManager.email_val(request.POST['email']):
			messages.error(request, 'Invalid Email or Email already exists', extra_tags='email')
			valid = False
		if not User.userManager.password_val(request.POST['password']):
			messages.error(request, 'Must be 8 characters or longer', extra_tags='password')
			valid = False
		if not User.userManager.confirm_val(request.POST['password'], request.POST['confirm']):
			messages.error(request, 'Password does not match', extra_tags='confirm')
			valid = False
		if not User.userManager.alias_val(request.POST['alias']):
			messages.error(request, 'Alias must be at least 2 characters, Letters and numbers, Space, Dash, and Underscore only')
			valid = False

		if valid:
			User.userManager.register_user(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['alias'])

			request.session['id'] = User.userManager.get_id(request.POST['email'], request.POST['password'])
			messages.success(request, 'registered.')

<<<<<<< HEAD
			return redirect(reverse('dash'))
		else:	
			return redirect(reverse('register'))

def dash(request):
	return render(request, 'login_reg_app/dashboard.html')

def profile(request):
	#get profile
	context={'profile': User.userManager.filter(id=request.session['id'])}

	return render(request, 'login_reg_app/profile.html', context)

def edit_profile(request):
	context={'profile': User.userManager.filter(id=request.session['id'])}
	return render(request, 'login_reg_app/editprofile.html', context)

def edit_name(request):
	valid = True
	if not User.userManager.name_val(request.POST['first']):
		messages.error(request, 'Name must be longer than 2 characters, Letters only', extra_tags='first_name')
		valid = False
		
	if not User.userManager.name_val(request.POST['last']):
		messages.error(request, 'Name must be longer than 2 characters, Letters only', extra_tags='last_name')
		valid = False
	
	if valid:
		User.userManager.filter(id=request.session['id']).update(first_name=request.POST['first'], last_name=request.POST['last'])

	return redirect(reverse('edit_profile'))

def edit_email(request):
	if not User.userManager.email_val(request.POST['email']):
		messages.error(request, 'Invalid Email or Email is the same', extra_tags='email')
	else:
		User.userManager.filter(id=request.session['id']).update(email=request.POST['email'])
	return redirect(reverse('edit_profile'))
=======
			return redirect(reverse('success'))
		else:
			return redirect(reverse('register'))

def success(request):
	return render(request, 'login_reg_app/success.html')

def dash(request):
	return render(request, 'login_reg_app/dash.html')
>>>>>>> 297e82e223fbb9a6e23ca76bdb14b079b128b31d
