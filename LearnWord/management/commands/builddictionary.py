from django.core.management.base import BaseCommand
from LearnWord.models import Word
from nltk.corpus import wordnet

class Command(BaseCommand):
    "Defines the builddictionary command"
    help = 'Builds the word dictionary database from the text file'

    def handle(self, *args, **options):
        # words.txt sourced from https://github.com/dwyl/english-words
        # words list includes 466k English words
        with open('media/words.txt', 'r') as input_file:
            for line in input_file:
                # Word in words.txt
                word = line.strip()
                # Definition from wordnet
                syns = wordnet.synsets(word)
                # Skipping words with no definition for now
                if syns:
                    w = Word(word=word, definition=syns[0].definition())
                    w.save()

        self.stdout.write(self.style.SUCCESS('Successfully created word database.'))
