import requests
import json
from giphy_api_key import api_key

def get_gifs_from_giphy(search_string,api_keys):
    #Returns data from Giphy API with up to 5 gifs corresponding to the search input"""
    baseurl = "https://api.giphy.com/v1/gifs/search"
    params="?q=" + search_string + "&api_key=" + api_key+"&limit=5"
    search=requests.get(baseurl + params)
    search_dict=json.dumps(search.text)
    strsearch=str(search_dict)
    print (strsearch)

a=get_gifs_from_giphy('Spongebob','ER6NNmR8hSAtvWrIivvYNHdo1US33WXJ')