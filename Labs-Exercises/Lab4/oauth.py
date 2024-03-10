import requests 

CLIENT_ID = "8566623798ce4e467245"  # Client ID from GITHUB after app creation.
CLIENT_SECRET = "710e2c26ec1a6547e8f72ab4da52391e08f0aa05"  # Client Secret from GITHUB.

REDIRECT_URL = "http://localhost.8080"  # Redirect URL for App.

def create_oauth_link():    # Method to create oauth link, no parameters.
    params = {  # These are all the required parameters the API expects (it's a dictionary).
        "client_id": CLIENT_ID, # giving 'client_id' key our CLIENT_ID var as value.
        "redirect_url": REDIRECT_URL, # giving 'redirect_url' key our REDIRECT_URL var as value.
        "scope": "user", # Github level of access, accesses basic user information.
        "response_type": "code", # Github app type of response, 
        # will receive authorization code as a response.

    }
    endpoint = "https://github.com/login/oauth/authorize"   # endpoint url for oauth page to authorize
    response = requests.get(endpoint, params=params)    # sends a get request to the oauth endpoint
    # with params dictionary above as the parameters. API Will automatically redirect you to GH website
    return response.url # returns the authorizaiton URL (URL of repsonse from GH / redirecting you to)

def exchange_code_for_access_token(code=None):  # oauth flow to exchange code for access token
    params = {
        "client_id": CLIENT_ID, # giving 'client_id' key our CLIENT_ID var as value.
        "client_secret": CLIENT_SECRET, # giving 'redirect_url' key our REDIRECT_URL var as value.
        "redirect_uri": REDIRECT_URL,   # Github level of access, accesses basic user information.
        "code": code,   # authorizaiton code received from github
    }

    headers = {"Accept": "application/json"}    # dictionary headers for the request. Accepts a json response 
    # due to "application/json".
    endpoint = "https://github.com/login/oauth/access_token"    # endpoint url to exchange authorization code
    # for an access token, endpoint from API.
    response = requests.post(endpoint, params=params, headers=headers).json()   
    #  makes post request to OAuth endpoint
    #  to exchange code for access token, 
    #  uses params dicitonary as params, and headers as headers. is a JSON object due to .json().
    # Here you have to send CLIENT_SECRET and code so that GH can validate code. Then GH API will geenrate an
    # access token and return it.
    return response["access_token"] # returns access token from response

def print_user_info(access_token=None): # Prints info about the authenticated user on GH like name & username
    headers = {"Authorization": f"token {access_token}"}    # headers dictionary, authorizaiton key with value 
    # of 'token {access_token}' to authenticate the request with the given access token.
    endpoint = "https://api.github.com/user"    # endpoint url provided info about the user. '/user/.
    response = requests.get(endpoint, headers=headers).json()   # sends get request to endpoint, using headers dict.
    # as headers param. JSON object due to .json().
    name = response["name"] # gets the user's name from the JSON object
    username = response["login"]    # gets user's username from JSON object
    private_repos_count = response["total_private_repos"]   # get's total private repo count from JSON object.
    print(
        f"{name} ({username}) | private repositories: {private_repos_count}"
    )   # prints all retrieved information from above.

link = create_oauth_link()  # calls create_oauth_link method
print(f"Follow the link to start the authentication with GitHub: {link}")
code = input("GitHub code: ")
access_token = exchange_code_for_access_token(code)
print(f"Exchanged code {code} with access token: {access_token}")
print_user_info(access_token=access_token)