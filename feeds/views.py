from django.shortcuts import render
from .models import *

# Create your views here.


def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myProjects = Project.objects.all()
    mySkills = Skill.objects.all()
    myContacts = Contact.objects.all()
    context = {
        "info": myinfo,
        "about": myabout,
        "projects": myProjects,
        "skills": mySkills,
        "contacts": myContacts,
    }

    return render(request, 'home_page.html', context)
