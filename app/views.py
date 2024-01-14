from django.shortcuts import render
from app.models import *
from django.contrib.auth.models import User


def index(r):
    user = User.objects.all().count()
    ctx = {
        'user': user
    }
    return render(r, 'dashboard/index.html', ctx)
