from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
import datetime
from django.contrib.auth.decorators import login_required  # Tambahkan baris ini
from django.core.exceptions import PermissionDenied        # Tambahkan baris ini
from django.contrib.auth.models import Group

# Create your views here.

from main.models import Experience, TechStack
from main.forms import ExperienceForm, TechStackForm

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')

    context = {
        "name": "Nafeeza Arwatabina",
        "npm": "2506604573",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Second year Undergraduate CS Student at Universitas Indonesia, " 
            "who eager to learn and find a sliver of hope amidst the hardship."
        ),
        "last_login": last_login,
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

@login_required(login_url="/login/") 
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

    experiences_json = serializers.serialize(
    "json", experiences, use_natural_foreign_keys=True)

    return HttpResponse(experiences_json, content_type="application/json")

@login_required(login_url="/login/") 
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")

    return redirect("main:show_experience")

def show_skills(request):
    json_response = get_skills_json(request)

    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    skills = [skill.object for skill in skills]

    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Nafeeza Arwatabina",
        "skill_technical" : "Technical",
        "skill_soft" : "Soft Skills",
        "skill_tool" : "Tools",
        "stack_list": skills,
        "title_query": title_query,
    }

    return render(request, "skills.html", context)

@login_required(login_url="/login/") 
def create_skill(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = TechStackForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill baru berhasil ditambahkan!")
        return redirect("main:show_skills")

    context = {
        "name": "Nafeeza Arwatabina",
        "skill_technical" : "Technical",
        "skill_soft" : "Soft Skills",
        "skill_tool" : "Tools",
        "form": form,
    }
    return render(request, "skills_form.html", context)

def get_skills_json(request):
    title_query = request.GET.get("title", "").strip()
    skills = TechStack.objects.all()

    if title_query:
        skills = skills.filter(title__icontains=title_query)

    skills_json = serializers.serialize(
    "json", skills, use_natural_foreign_keys=True)
    
    return HttpResponse(skills_json, content_type="application/json")

@login_required(login_url="/login/") 
def delete_skill(request, skill_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    skill = get_object_or_404(TechStack, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")

    return redirect("main:show_skills")

def update_skill(request, skill_id):
    skill = get_object_or_404(TechStack, pk=skill_id)

    if request.method == "POST":
        form = TechStackForm(request.POST, instance=skill)

        if form.is_valid():
            form.save()
            messages.success(request, "Skill berhasil di update!")
            return redirect("main:show_skills")
        
    else:
        form = TechStackForm(instance=skill)
    
        context = {
            "name": "Nafeeza Arwatabina",
            "skill_technical" : "Technical",
            "skill_soft" : "Soft Skills",
            "skill_tool" : "Tools",
            "form": form,
            "skill": skill,
        }
        return render(request, "update_skill.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Nafeeza",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect("main:show_main")
        current_time =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        response.set_cookie('last_login', current_time)
        return response

    context = {
        "name": "Nafeeza",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, skill_id):
    skill = get_object_or_404(TechStack, pk=skill_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in skill.starred_by.all():
            skill.starred_by.remove(request.user)
        else:
            skill.starred_by.add(request.user)

    return redirect("main:show_skills")

def is_editor(request):
    return request.user.groups.filter(name='Editor').exists()