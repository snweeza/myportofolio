from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience
from main.models import TechStack


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="VPIC Bisdev SIWAK-NG",
            description="Bertanggung jawab dalam pengembangan bisnis SIWAK-NG.",
            category="volunteer",
        )
        self.techstack = TechStack.objects.create(
            title="HTML",
            level="Learning",
            icon_url="https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/html-icon.png", 
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "VPIC Bisdev SIWAK-NG")
        self.assertEqual(self.experience.category, "volunteer")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Volunteer")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    def test_techstack_model(self):
            self.assertEqual(str(self.techstack), "HTML")
            self.assertEqual(self.techstack.level, "Learning")
            self.assertEqual(self.techstack.icon_url, "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/html-icon.png")

    def test_techstack_page(self):
            response = self.client.get(reverse("main:show_techstack"))
    
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "techstack.html")
            self.assertContains(response, self.techstack.title)
            self.assertContains(response, "Learning")
            self.assertContains(response, "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/html-icon.png")

    def test_empty_ts_page(self):
            TechStack.objects.all().delete()
            response = self.client.get(reverse("main:show_techstack"))
    
            self.assertContains(response, "Belum ada skill yang ditambahkan.")