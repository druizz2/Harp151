DictionaryAPI Wrapper

endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/"

How to use:
1. Import the file

get_definition:

The get_definition method asks the user to input a word, then makes a json request
and accesses the 0th index of the list in the json object, then the 'meanings' key 
(that has a nested list-dictionary as the value), then the definitions dictionary (has a list has the value), 
then the 0th index of value list, and then finally the 
'definition' key (i.e the definition of the word).

get_pronunciation:

The get_pronunciation method asks the user to input a word then makes a json request
and accesses the 0th index of the list in the json object, then the 'phonetics' key
(that has a nested list-dictionary as the value), then the 1st index, and then finally 
the "text" key.

get_audio_link:

The get_audio_link method asks the user to input a word then makes a json request
and accesses the 0th index of the list in the json object, then the 'phonetics' key, the the 
0th index, and then finally the 'audio' key. 