from django.test import TestCase
from django.urls import reverse
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

class GalleryViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Nature')
        self.image = Image.objects.create(
            title='Sunset',
            image=SimpleUploadedFile('sunset.jpg', b'image data', content_type='image/jpeg'),
            created_date=date.today(),
            age_limit=0
        )
        self.image.categories.add(self.category)

    def test_gallery_view_status_code(self):
        response = self.client.get(reverse('main'))  
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_template_used(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'gallery.html')

    def test_gallery_view_context_contains_category(self):
        response = self.client.get(reverse('main'))
        self.assertIn(self.category, response.context['categories'])


class ImageDetailViewTests(TestCase):
    def setUp(self):
        self.image = Image.objects.create(
            title='Sunset',
            image=SimpleUploadedFile('sunset.jpg', b'image data', content_type='image/jpeg'),
            created_date=date.today(),
            age_limit=0
        )

    def test_image_detail_view_status_code(self):
        response = self.client.get(reverse('image_detail', args=[self.image.pk])) 
        self.assertEqual(response.status_code, 200)

    def test_image_detail_view_template_used(self):
        response = self.client.get(reverse('image_detail', args=[self.image.pk]))
        self.assertTemplateUsed(response, 'image_detail.html')

    def test_image_detail_view_context_contains_image(self):
        response = self.client.get(reverse('image_detail', args=[self.image.pk]))
        self.assertEqual(response.context['image'], self.image)
