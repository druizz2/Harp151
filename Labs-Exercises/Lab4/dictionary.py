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

    def play_audio_link(self, link):
        # Citation: https://stackoverflow.com/questions/38171169/how-to-play-mp3-from-url
        # I used VLC here. In order for the audio to actually play, you must have VLC  installed 
        # or you will get an error at runtime.
        self.link = link
        link_play = vlc.MediaPlayer(link)
        link_play.play()

    def get_audio_link(self):
        try:
            word = input("Enter a word: ")
            word_request = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()
            get_word_audio_link = word_request[0]["phonetics"][0]["audio"]
            print(f"The audio link is '{get_word_audio_link}'. ")
            play_audio = input("Play the audio link? (Y/N): ")
            if play_audio == 'Y':
                self.play_audio_link(get_word_audio_link)
            elif play_audio == 'N':
                pass
            else:
                print("Invalid input. ")
        except IndexError:
            print("Index Error. Unable to retrieve the audio link of the word. ")
        except KeyError:
            print("Key Error. Try entering a different word. ")
 
if __name__ == "__main__":
    instance = DictionaryAPI()
    instance.get_definition()
    instance.get_pronunciation()
    instance.get_audio_link()


