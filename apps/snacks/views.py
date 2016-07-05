from django.shortcuts import render, redirect

from models import User, Snack
# Create your views here.
def snack_request(request, id):
	if request.method == 'POST':
		snack_tuple = Snack.snackManager.snack_request(request.POST['snack_request'], request.session['id'])
	return render (request, '/benefits.html')
