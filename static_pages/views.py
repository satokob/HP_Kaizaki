from django.shortcuts import render

def about(request):
  return render(request, 'about/about.html')

def plan(request):
  return render(request, 'plan/plan.html')