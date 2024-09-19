from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
class News(models.Model):
  title = models.CharField(max_length=200)
  content = RichTextField()
  published_date = models.DateField(null=True, blank=True, default=timezone.now)

  def __str__(self):
    snippet = self.content[:50]  
    return f"{self.title} - {snippet}... ({self.published_date.strftime('%Y-%m-%d')})"
