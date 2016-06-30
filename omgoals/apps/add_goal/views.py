from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import User, Goal, GoalAnimal
from django.contrib import messages

def add_goal(request):
	return render(request, 'add_goal.html')

def insert_goal(request):
	Goal.goalManager.insert_goal(request.POST['title'], request.POST['description'], request.POST['due_date'], request.POST['priority'], request.POST['category'], request.session['id'], request.POST['animal_name'])

	return redirect(reverse('dash'))
