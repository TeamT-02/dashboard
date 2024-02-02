from django.shortcuts import render
from main.models import *


def home(request):
    base = Home.objects.order_by('-id')[:1]
    statik = Statik.objects.order_by('-id')[:4]
    left = Problems_left.objects.order_by('-id')[:1]
    right = Problems_right.objects.order_by('-id')[:1]
    social = Social_Networks.objects.order_by('-id')[:1]
    social_link = Social_Networks_link.objects.order_by()
    website = Website_update.objects.order_by('-id')[:1]
    action = Deadline.objects.all()
    company = Company_mobile_download_info.objects.order_by('-id')[:1]
    stis = Statistika.objects.order_by('-id')[:1]
    ctx = {
        'base': base,
        'statik': statik,
        'left': left,
        'right': right,
        'social': social,
        'social_link': social_link,
        'website': website,
        'action': action,
        'company': company,
        'stis':stis
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('text')
        con = Contact(
            name=name,
            email=email,
            subject=subject,
            text=text
        )
        con.save()
    return render(request, 'main/index.html', ctx)
