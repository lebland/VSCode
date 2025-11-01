from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField("Titre", max_length=200)
    date = models.DateTimeField("Date et heure")
    location = models.CharField("Lieu", max_length=200)
    description = models.TextField("Description")
    created_at = models.DateTimeField("Date de création", auto_now_add=True)
    updated_at = models.DateTimeField("Dernière modification", auto_now=True)
    
    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
        ordering = ['date']  # Tri par date par défaut
    
    def __str__(self):
        return f"{self.title} ({self.date.strftime('%d/%m/%Y')})"
    
    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])