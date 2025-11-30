from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bird(models.Model):
    """A bird the user wants to record."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a bird."""
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        if (len(self.text) > 50):
            return f"{self.text[:50]}..."
        return f"{self.text[:50]}"
