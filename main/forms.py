from django.forms import ModelForm, TextInput, Textarea, URLInput, DateTimeInput

from main.models import Experience
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "photo",
            "ended_at"
        ]

        labels = {
            "title": "Nama Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "photo": "URL Gambar Pengalaman",
            "ended_at": "Tanggal Berakhir",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Software Engineering Intern at Samsung",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Pengalamanmu",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "volunteer, part-time, full-time",
                }
            ),
            "photo": URLInput(
                attrs={
                    "placeholder" : "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "placeholder": "YYYY-MM-DD HH:MM",
                }
            ),
        }