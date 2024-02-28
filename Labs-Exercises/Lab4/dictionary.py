import requests
import json

endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_definition():
    word = input("Enter a word: ")
    word_request = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()
    print(json.dumps(word_request))
   
def get_pronunciation():
    pass

get_definition()
