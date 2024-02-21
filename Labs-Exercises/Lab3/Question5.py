import requests 
import random
import json
"""
The API I chose was Riot Games Developer API. The API returns various data
about which ever game you choose. The API does not require payment, but if 
you want to use it for prouduct or larger scale reasons, you need to submit 
an application request to Riot Games and be approved. The API does require a key.
For this use, I will be utilizing their API to fetch League of Legendscharacter/champion 
data.
Here is a link to it: https://developer.riotgames.com
"""

base_url = "https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/"

# First I create a method that fetches all character/champions & their data. 
# This will return all champions and their data like name, hp, damage, etc.
def get_all_champions():
    all_champions_url = "https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json"
    get_all_request = requests.get(all_champions_url)
    get_all_json = get_all_request.json()
    print(get_all_json)
# get_all_champions()

# This method will return champion specific data like name, description, health, damage, etc.
def get_champion(champion_name):
    champions_url = f"https://ddragon.leagueoflegends.com/
    cdn/14.3.1/data/en_US/champion/{champion_name}.json"
    get_champion_request = requests.get(champions_url)
    get_champion_json = get_champion_request.json()
    print(get_champion_json)
# This method just chooses a random champion to be used in the above method
def random_champion():
    champions = ["Zed", "Jayce", "Yasuo", "Irelia", "Warwick", "Viego", "Ryze"]
    random_choice = random.choice(champions)
    return random_choice

get_champion(random_champion())