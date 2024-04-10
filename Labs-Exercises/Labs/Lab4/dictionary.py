import requests
import json
import vlc

class DictionaryAPI:

    endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def get_definition(self):
        try:
            word = input("Enter a word: ")
            word_request = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()
            get_word_def = word_request[0]["meanings"][0]["definitions"][0]["definition"]
            print(get_word_def)
        except IndexError:
            print("Index Error. Unable to retrieve the definition. ")
        except KeyError:
            print("Key Error. Try entering a different word. ")
            
            
    def get_pronunciation(self):
        try:
            word = input("Enter a word: ")
            word_request = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()
            get_word_pronunciation = word_request[0]["phonetics"][1]["text"]
            print(get_word_pronunciation.replace('/', ''))
        except IndexError:
            print("Index Error. Unable to retrieve the pronunciation. ")
        except KeyError:
            print("Key Error. Try entering a different word. ")


    def get_audio_link(self):
        try:
            word = input("Enter a word: ")
            word_request = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()
            get_word_audio_link = word_request[0]["phonetics"][0]["audio"]
            print(f"The audio link is '{get_word_audio_link}'. ")
        except IndexError:
            print("Index Error. Unable to retrieve the audio link of the word. ")
        except KeyError:
            print("Key Error. Try entering a different word. ")
 
if __name__ == "__main__":
    instance = DictionaryAPI()
    instance.get_definition()
    instance.get_pronunciation()
    instance.get_audio_link()


