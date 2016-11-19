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

        self.begin_words = {
            'I went to an Ivy League school.' : (0.1, None),
            'Excuse me,' : (0.40, None),
            'I\'m, like, a really smart person.': (0.2, 'Look what I built - something truly classy, Trump Tower'),
            'Believe me, ': (0.35, 'It\'s gonna be yuge!'),
            'Well, first I have to say one thing, very important.': (0.3, None),
            'I know the Chinese. I\'ve made a lot of money with the Chinese. I understand the Chinese mind.':(0.2, None),
            'Wrong. Wrong.': (0.3, 'No, you\'re wrong.'),
            'That\'s called business, by the way.' : (0.2, None),
            'I have a great relationship with the blacks.' : (0.3, None),
            'I don\'t think I\'m going to lose.' : (0.1, None),
            'I put my name on buildings because it sells better.' : (0,2, None),
            'I know more about ISIS than the generals do, believe me.' : (0.2, 'I would bomb the sh**t out of them.'),
            'The only difference between me and the other candidates is that I’m more honest and my women are more beautiful.' : (0.2, None),
            'We\'re going to win.' : (0.3, None),
            'I do not wear a "wig". My hair may not be perfect but it\'s mine.' : (0.2, None),
            'When I think I\'m right, nothing bothers me.' : (0.25, None),
            'We can\'t continue to allow China to rape our country.' : (0.35, 'I never said that. I didn\'t say that'),
            'Look, I\'m worth $10 billion.' (0.3, 'Part of the beauty of me is that I am very rich.'),
            'You\'re fired!' (0.25, 'Oh really?'),
            'I don\'t know what will happen, but it will be interesting.' : (0.15, None),
            'Let me just tell you.' : (0.2, 'Ugh'),
            'I will be so good at the military your head will spin.' : (0.2, None),
            'Nobody respects women more than me.' : (0.3, 'Such a nasty woman'),
            'We will be a country of LAW and ORDER!' : (0.2, None),
            'I don\'t have a racist bone in my body.' : (0.3, None),
            'Do you mind if I sit back a little bit because your breath is very bad. It really is.' : (0.35, None),
            'I would bomb the hell out of those oilfields.' : (0.2, None),
            'Why can\'t we use nuclear weapons?' : (0.2, 'We\'re going to win'),
            'I will be the greatest jobs president that God ever created.' : (0.1, None),
            'We should just cancel the election and just give it to Trump.' : (0.15, None),
            'When Mexico sends its people, they\'re sending people that have lots of problems.' : (0.2, 'They\'re bringing drugs and crimes. They\'re rapists.'),
            
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
