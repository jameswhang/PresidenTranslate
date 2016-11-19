from quote_service import QuoteService
from math import floor
import random

class TranslationService(object):
    def __init__(self, president): 
        self.qs = QuoteService(president)
        self.quotes = self.qs.getQuotes()
        self.words = self.qs.getWords() 

        self.end_words = [
                'Make America great again.',
                'LAWW and ORRRDER.',
                'It\'s gonna be yuge!',
                'We need to build a wall on the Mexican border.',
                
        ]

        self.assoc_words = {
                'china': self.china_words
        }
        self.begin_words = {
            'I went to an Ivy League school.' : (0.1, None),
            'Excuse me,' : (0.40, None),
            'I\'m, like, a really smart person.': (0.2, 'Look what I built - something truly classy, Trump Tower'),
            'Believe me, ': (0.35, 'It\'s gonna be yuge!'),
            'Well, first I have to say one thing, very important.': (0.3, None),
            'I know the Chinese. I\'ve made a lot of money with the Chinese. I understand the Chinese mind', (0.2, None),
        }


    def add_mannerisms(self, text):
        sentences = text.split('.')
        translated_sentences = ''
        for sentence in sentences:
            if len(sentence) <= 1:
                continue
            added_mannerism = False
            added_end_words = False
            randnum = random.random()
            for mannerism in self.begin_words.keys():
                man_info = self.begin_words[mannerism]
                if randnum < man_info[0]:
                    translated_sentences += (mannerism + sentence + '.')

                    if random.random() < 0.5 and man_info[1] is not None:
                        translated_sentences += man_info[1]
                        added_end_words = True
                    added_mannerism = True
                    break

            if not added_mannerism:
                translated_sentences += sentence + '.'
            
            if not added_end_words and random.random() < 0.2:
                end_word = self.end_words[int(floor(random.random() * len(self.end_words)))]
                translated_sentences += end_word
        return translated_sentences

    def translate(self, text):
        # Simple word replace
        for word in self.words.keys():
            text = text.replace(word, self.words[word])

        # Parse remaining sentence and add mannerisms
        text = self.add_mannerisms(text)
        return text
