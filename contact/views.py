from django.shortcuts import render
from .forms import ContactForm

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_calid():
      pass

  else:
    form = ContactForm()

  return render(request, 'contact/contact.html', {'form' : form})
