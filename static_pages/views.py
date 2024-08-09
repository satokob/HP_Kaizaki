from django.shortcuts import render

def about(request):
  return render(request, 'static_pages/about.html')

def plan(request):
  return render(request, 'static_pages/plan.html')