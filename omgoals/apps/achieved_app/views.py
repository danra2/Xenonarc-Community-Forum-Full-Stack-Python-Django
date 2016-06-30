from django.shortcuts import render
from .models import Achieved

def achieved_page(request):
	context={'achieved': Achieved.objects.all()}
	return render(request, 'achieved_app/achieved.html', context)