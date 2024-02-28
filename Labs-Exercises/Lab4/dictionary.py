import requests
import json

endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_definition():
    word = input("Enter a word: ")
    word_def = (requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")).json
    print(word_def)
def get_pronunciation(word):
    pass
print("test")
get_definition()
