from django.contrib import admin
from main.models import Experience, TechStack

# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')
    search_fields = ('title',)

admin.site.register(TechStack)