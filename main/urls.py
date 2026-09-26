from django.urls import path

from main.views import show_main, show_experience, show_skills, create_experience, get_experiences_json, delete_experience, create_skill, get_skills_json, delete_skill
from main.views import update_skill, register, logout_user, login_user, toggle_star

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experiences/", show_experience, name="show_experience"),
    path("skills/", show_skills, name="show_skills"), 
    path("experiences/add/", create_experience, name="create_experience"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience ,name="delete_experience"),
    path("skills/add/", create_skill, name="create_skill"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    path("skill/<uuid:skill_id>/delete/", delete_skill ,name="delete_skill"),
    path("skills/<uuid:skill_id>/update/",update_skill, name="update_skill"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("skills/<uuid:skill_id>/star/", toggle_star, name="toggle_star"),
]