from django.db import models
from django.utils import timezone

# Create your models here.


class MovieVarity(models.Model):
    MOVIE_TYPE_CHOICE= [
        ('KA','KARAN ARJUN'),
        ('BM','BATMAN'),
        ('SM','SUPPERMAN'),
        ('SM','SPIDERMAN'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movie/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=MOVIE_TYPE_CHOICE, default='KA')

    def __str__(self):
        return self.name
    