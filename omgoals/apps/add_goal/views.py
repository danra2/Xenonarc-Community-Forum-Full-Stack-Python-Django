from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
from django.contrib import messages

def add_goal(request):
	return render(request, 'add_goal.html')
