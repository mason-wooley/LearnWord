import random
from django.http import HttpResponse
from django.shortcuts import render
from .models import Word

def index(request):
    word_count = Word.objects.count()
    random.seed()
    word_id = random.randint(1, word_count)
    word = Word.objects.get(id=word_id)
    return HttpResponse("%s — %s" % (word.word, word.definition))
