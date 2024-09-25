from django.shortcuts import render
from .instagram_api import get_instagram_posts 

def gallery(request):
  instagram_posts = get_instagram_posts()
  return render(request, 'gallery/gallery.html', {'instagram_posts': instagram_posts})
