from django.shortcuts import render

def achieved_page(request):
	return render(request, 'achieved_app/achieved.html')