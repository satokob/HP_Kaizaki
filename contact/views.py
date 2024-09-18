from django.shortcuts import render
from .forms import ContactForm
import logging

logger = logging.getLogger(__name__)

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.send_email()
      logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
      return render(request, 'contact/contact_success.html', {'form': form})

  else:
    form = ContactForm()

  return render(request, 'contact/contact.html', {'form' : form})
