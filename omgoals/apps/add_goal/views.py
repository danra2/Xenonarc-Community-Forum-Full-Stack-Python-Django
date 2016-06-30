from django.shortcuts import render

def add(request):
	return render(request, 'add_goal/add.html')