from django.contrib import messages
from django.shortcuts import render, redirect
from app.models import *
from django.contrib.auth.models import User
from main.models import *
from django.views.generic.edit import CreateView


def index(r):
    user = User.objects.all().count()
    ctx = {
        'user': user
    }
    return render(r, 'dashboard/index.html', ctx)


def forms(r):
    return render(r, 'dashboard/form.html')


def ADD_HOME(request):
    if request.method == "POST":
        images = request.POST.get('images')
        title = request.POST.get('title')
        text = request.POST.get('text')
        home = Home(
            images=images,
            title=title,
            text=text,
        )
        home.save()
        # print(home)
        messages.success(request, 'gap yu')
        return redirect('view_home')
    return render(request, 'crud/home/create_home.html')


def VIEW_HOME(request):
    view_home = Home.objects.all()
    ctx = {
        'view_home': view_home
    }
    return render(request, 'crud/home/view_home.html', ctx)


def EDIT_HOME(request, id):
    home_edit = Home.objects.filter(id=id)
    ctx = {
        'home_edit': home_edit
    }
    return render(request, 'crud/home/edit_home.html', ctx)


def UPDATE_HOME(request):
    if request.method == "POST":
        id_home = request.POST.get('id')
        images = request.POST.get('images')
        title = request.POST.get('title')
        text = request.POST.get('text')
        home = Home(
            id_home=id_home,
            images=images,
            title=title,
            text=text,
        )
        home.save()
        # print(home)
        messages.success(request, 'gap yu')
    return redirect('view_home')


def DELETE_HOME(request, id):
    session = Home.objects.get(id=id)
    session.delete()
    messages.success(request, "zo'r uchirdiz A !")
    return redirect('view_home')


def ADD_STATIK(request):
    if request.method == "POST":
        number = request.POST.get('number')
        name = request.POST.get('name')
        statik = Statik(
            number=number,
            name=name
        )
        statik.save()
        messages.success(request, 'gap yuq')
        return redirect('view_statik')
    return render(request, 'crud/statik/add_statik.html')


def VIEW_STATIK(request):
    view_statik = Statik.objects.all()
    ctx = {
        'view_statik': view_statik
    }
    return render(request, 'crud/statik/view_statik.html', ctx)


def EDIT_STATIK(request, id):
    edit_statik = Statik.objects.filter(id=id)
    ctx = {
        'edit_statik': edit_statik
    }
    return render(request, 'crud/statik/edit_statik.html', ctx)


def UPDATE_STATIK(request):
    if request.method == "POST":
        number = request.POST.get('number')
        name = request.POST.get('name')
        statik = Statik(
            number=number,
            name=name
        )
        statik.save()
        messages.success(request, 'gap yuq')
    return redirect('view_statik')


def DELETE_STATIK(request, id):
    session = Statik.objects.get(id=id)
    session.delete()
    messages.success(request, "zo'r uchirdiz A !")
    return redirect('view_statik')


def ADD_PROBLEMS(request):
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        images = request.POST.get('images')
        problems = Problems_left(
            title=title,
            text=text,
            images=images
        )
        problems.save()
        return redirect('index')
    return render(request, 'crud/problems/add_problems.html')


def ADD_PROBLEMSr(request):
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        images = request.POST.get('images')
        problems = Problems_right(
            title=title,
            text=text,
            images=images
        )
        problems.save()
        return redirect('view_problems')
    return render(request, 'crud/problems/add_problems.html')


def VIEW_PROBLEMS(request):
    problems_right = Problems_right.objects.all()
    problems_left = Problems_left.objects.all()
    ctx = {
        "problems_left": problems_left,
        'problems_right': problems_right
    }
    return render(request, 'crud/problems/view_problems.html', ctx)


def EDIT_PROBLEMS(request, id):
    problems = Problems_left.objects.filter(id=id)
    problemsr = Problems_right.objects.filter(id=id)
    ctx = {
        'problemsr': problemsr,
        'problems': problems
    }
    return render(request, 'crud/problems/edit_problems.html', ctx)


def EDIT_PROBLEMSr(request, id):
    problemsr = Problems_right.objects.filter(id=id)
    ctx = {
        'problemsr': problemsr,
    }
    return render(request, 'crud/problems/edit_problemsr.html', ctx)


def UPDATE_PROBLEMS(request):
    if request.method == "POST":
        title = request.POST.get('title')
        images = request.POST.get('images')
        text = request.POST.get('text')
        problems = Problems_left(
            title=title,
            images=images,
            text=text
        )
        problems.save()
    return redirect('view_problems')


def UPDATE_PROBLEMSr(request):
    if request.method == "POST":
        title = request.POST.get('title')
        images = request.POST.get('images')
        text = request.POST.get('text')
        problems = Problems_right(
            title=title,
            images=images,
            text=text
        )
        problems.save()
    return redirect('view_problems')


def DELETE_PROBLEMS(request, id):
    session = Problems_left.objects.get(id=id)
    session.delete()
    messages.success(request, "zo'r uchirdiz A !")
    return redirect('view_statik')


def DELETE_PROBLEMSr(request, id):
    session = Problems_right.objects.get(id=id)
    session.delete()
    messages.success(request, "zo'r uchirdiz A !")
    return redirect('view_statik')


def ADD_SOCIAL(request):
    if request.method == "POST":
        images = request.POST.get('images')
        title = request.POST.get('images')
        text = request.POST.get('text')
        social = Social_Networks(
            images=images,
            title=title,
            text=text
        )
        social.save()
        return redirect('view_social')
    return render(request, 'crud/social_networks/add_social.html')


def VIEW_SOCIAL(request):
    social = Social_Networks.objects.all()
    ctx = {
        'social': social
    }
    return render(request, 'crud/social_networks/view_social.html', ctx)


def EDIT_SOCIAL(request, id):
    social = Social_Networks.objects.filter(id=id)
    ctx = {
        'social': social
    }
    return render(request, 'crud/social_networks/edit_social.html', ctx)


def UPDATE_SOCIAL(request):
    if request.method == "POST":
        images = request.POST.get('images')
        title = request.POST.get('images')
        text = request.POST.get('text')
        social = Social_Networks(
            images=images,
            title=title,
            text=text
        )
        social.save()
    return redirect('view_social')


def DELETE_SOCIAL(request, id):
    session = Social_Networks.objects.get(id=id)
    session.delete()
    messages.success(request, "zo'r uchirdiz A !")
    return redirect('view_statik')


def ADD_SOCIAL_LINK(request):
    social = Social_Networks_link.objects.all()
    ctx = {
        'social': social
    }
    if request.method == "POST":
        forkey = request.POST.get('forkey')
        insta = request.POST.get('insta')
        teleg = request.POST.get('teleg')
        telebot = request.POST.get('telebot')
        link = Social_Networks_link(
            forkey=forkey,
            instagram_link=insta,
            telegram_link=teleg,
            telegram_bot=telebot
        )
        link.save()
        return redirect('view_home')
    return render(request, 'crud/social_link/add_social.html', ctx)


def VIEW_SOCIAL_LINK(request):
    social_link = Social_Networks_link.objects.all()
    ctx = {
        'social_link': social_link
    }
    return render(request, 'crud/social_link/view_social.html', ctx)


def EDIT_SOCIAL_LINK(request, id):
    edit_social = Social_Networks_link.objects.filter(id=id)
    ctx = {
        'edit_social': edit_social
    }
    return render(request, 'crud/social_link/edit_social.html', ctx)


def UPDATE_SOCIAL_LINK(request):
    if request.method == "POST":
        forkey = request.POST.get('forkey')
        insta = request.POST.get('insta')
        teleg = request.POST.get('teleg')
        telebot = request.POST.get('telebot')
        link = Social_Networks_link(
            forkey=forkey,
            instagram_link=insta,
            telegram_link=teleg,
            telegram_bot=telebot
        )
        link.save()
        return redirect('view_home')


def DELETE_SOCIAL_LINK(request, id):
    session = Social_Networks_link.objects.get(id=id)
    session.delete()
    messages.success(request, "zo'r uchirdiz A !")
    return redirect('view_statik')
