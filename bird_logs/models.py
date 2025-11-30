from django.db import models
from django.contrib.auth.models import User

class Bird(models.Model):
    """A bird the user wants to record."""

    COLOR_CHOICES = [
        ('black', 'Black'),
        ('white', 'White'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
        ('red', 'Red'),
        ('orange', 'Orange'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('purple', 'Purple'),
        ('pink', 'Pink'),
        ('mixed', 'Mixed/Multiple'),
    ]

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    main_color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='mixed')
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ['text', 'owner']

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Sighting(models.Model):
    """Log when/where the user saw a bird"""
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
    sighting_date = models.DateField()
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'sightings'

    def __str__(self):
        """Return a simple string representing the sighting."""
        if (len(self.text) > 50):
            return f"{self.text[:50]}..."
        return f"{self.text[:50]}"
