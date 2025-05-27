# functions/get_all_posts.py

import requests

def get_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch posts"}
