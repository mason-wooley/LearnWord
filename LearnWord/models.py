import datetime

from django.db import models

class Word(models.Model):
    def __str__(self):
        return self.word
    
    # Longest word currently is 37 characters
    word = models.CharField(max_length=50)
    # Longest definition currently is 479 characters with only 5 words over 400
    definition = models.CharField(max_length=480)
