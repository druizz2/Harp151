import requests
import json
"""
The API I chose was the open source Hyrule Compendium for The Legend of Zelda Breath
of The Wild & TOTK. Since the API is open source, it does not require any form of payment. 
The API also does not require a key. The API is composed of two API's, the compendium API, 
and a smaller regions API (they return different info/data).
Here is a link to it: https://gadhagod.github.io/Hyrule-Compendium-API/#/
"""
base_url_compendium = "https://botw-compendium.herokuapp.com/api/v3/compendium/"
base_url_regions = "https://botw-compendium.herokuapp.com/api/v3/regions/"

"""
I will be doing one sample call using the compendium API, and one using the reigons API
"""
# compendium call -> Here we are retrieving data on a specific monster in the game, the bokoblin. 
# All we need to do is add /entry/bokoblin to the base url. This call is specific to the bokoblin since we
# entered it. The API also supports things like weapons, items, equipment, treasure, etc.
compendium_bokoblin_url = "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/bokoblin"
get_bokoblin_call = requests.get(compendium_bokoblin_url)
bokoblin_json = get_bokoblin_call.json()
print(bokoblin_json)

# regions call -> Here we are retrieving data on a specific region in the game, Hateno.
# All we need to do is add the region name to the base url.
hateno_region_url = "https://botw-compendium.herokuapp.com/api/v3/regions/hateno"
get_hateno_region = requests.get(hateno_region_url)
hateno_region_json = get_hateno_region.json()
print(hateno_region_json)