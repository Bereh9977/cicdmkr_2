from django.shortcuts import render, get_object_or_404
from .models import Category, Image

def gallery_view(request):
    categories = Category.objects.prefetch_related('image_set').all()
    return render(request, 'gallery.html', {'categories': categories})