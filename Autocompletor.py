import string
import nltk
from nltk.corpus import stopwords
import requests


class Autocompletor:

    def __init__(self):
        self.words_dictionary = {}
        self.stopwords = stopwords.words("english")

    def build_dictionary(self, text):

        text = text.replace("\n", "").translate(str.maketrans('', '', string.punctuation)).lower()

        for token in nltk.word_tokenize(text):
            if token is 'me':
                print("me")
            if token not in self.stopwords:
                if token is "me":
                    print("bad")
                if token in self.words_dictionary:
                    self.words_dictionary[token] += 1
                else:
                    self.words_dictionary.update({token: 1})

    def search_top_k_strings(self, prefix, k=10):
        top_k_strings = {}
        for token in self.words_dictionary:
            if token.startswith(prefix):
                freq = self.words_dictionary[token]
                if len(top_k_strings.keys()) < k:
                    top_k_strings.update({token: freq})
                else:
                    for top_string in top_k_strings:
                        if freq > top_k_strings[top_string]:
                            top_k_strings.pop(top_string)
                            top_k_strings.update({top_string: freq})

        return sorted(top_k_strings, key=top_k_strings.get, reverse=True)



