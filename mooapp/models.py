from django.db import models

class Cow(models.Model):
    said = models.CharField(max_length=160)

    def __str__(self):
        return self.said
