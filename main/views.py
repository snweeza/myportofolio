from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

from main.models import Experience, TechStack
from main.forms import ExperienceForm


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
    json_response = get_experiences_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Nafeeza Arwatabina",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def show_techstack(request):
    context = {
        "name": "Nafeeza Arwatabina",
        "skill_technical" : "Technical",
        "skill_soft" : "Soft Skills",
        "skill_tool" : "Tools",
        "stack_list": TechStack.objects.all(),
    }
    return render(request, "techstack.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Nafeeza Arwatabina",
        "form": form,
    }
    return render(request, "experiences_form.html", context)

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")