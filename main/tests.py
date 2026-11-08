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
            category="Technical",
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

    def test_techstack_model(self):
            self.assertEqual(str(self.techstack), "HTML")
            self.assertEqual(self.techstack.category, "Technical")
            self.assertEqual(self.techstack.icon_url, "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/html-icon.png")
