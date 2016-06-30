from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..login_reg_app.models import User
from django.contrib import messages

def journal(request):
    return render(request, 'journal.html')