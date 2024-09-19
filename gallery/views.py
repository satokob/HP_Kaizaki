from django.shortcuts import render
from .instagram_api import get_instagram_posts 

def gallery(request):
  return render(request, 'gallery/gallery.html')
