from django.urls import path

from main.views import show_main, show_experience, show_techstack, create_experience, get_experiences_json, delete_experience

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experiences/", show_experience, name="show_experience"),
    path("skills/", show_techstack, name="show_techstack"), 
    path("experiences/add/", create_experience, name="create_experience"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience ,name="delete_experience"),
]