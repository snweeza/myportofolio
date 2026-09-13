from django.shortcuts import render

# Create your views here.

from main.models import Experience
from main.models import TechStack


def show_main(request):
    context = {
        "name": "Nafeeza Arwatabina",
        "npm": "2506604573",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Second year Undergraduate CS Student at Universitas Indonesia, " 
            "who eager to learn and find a sliver of hope amidst the hardship."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nafeeza Arwatabina",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_techstack(request):
    context = {
        "name": "Nafeeza Arwatabina",
        "skill_competent" : "Competent",
        "skill_learning" : "Learning",
        "stack_list": TechStack.objects.all(),
    }
    return render(request, "techstack.html", context)