TRUMP = 'T'
OBAMA = 'O'

class QuoteService(object):
    def __init__(self, president):
        if president == TRUMP:
            self.quotes = [
                "Some quote"
            ]
            self.words = {
                "huge": "yuge",
                "big": "bigly",
                "dumb": "moron",
            }

        else:
            self.quotes = [
                "Obama quotes"
            ]
            self.words = {
                "boo": "vote"
            }

    def getQuotes(self):
        return self.quotes

    def getWords(self):
        return self.words
