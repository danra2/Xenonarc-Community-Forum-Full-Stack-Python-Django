from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import User, Goal, GoalAnimal, Milestone
from django.contrib import messages

def add_goal(request):
	return render(request, 'add_goal.html')

def insert_goal(request):
	print request.POST['category']

	Goal.goalManager.insert_goal(request.POST['title'], request.POST['description'], request.POST['due_date'], request.POST['priority'], request.POST['category'], request.session['id'], request.POST['animal_name'])

	this_goal = Goal.objects.get(title=request.POST['title'], description=request.POST['description'])

	if (request.POST['milestone1'] != ""):
		Milestone.milestoneManager.insert_milestone(request.POST['milestone1'], this_goal.id)

	try:
		Milestone.milestoneManager.insert_milestone(request.POST['milestone2'], this_goal.id)
	except:
		pass

	try:
		Milestone.milestoneManager.insert_milestone(request.POST['milestone3'], this_goal.id)
	except:
		pass

	try:
		Milestone.milestoneManager.insert_milestone(request.POST['milestone4'], this_goal.id)
	except:
		pass

	try:
		Milestone.milestoneManager.insert_milestone(request.POST['milestone5'], this_goal.id)
	except:
		pass

	try:
		Milestone.milestoneManager.insert_milestone(request.POST['milestone6'], this_goal.id)
	except:
		pass



	return redirect(reverse('dash'))
