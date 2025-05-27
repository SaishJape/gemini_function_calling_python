# # ✅ functions/get_post_by_title.py

import requests

# def get_post_by_title(title: str) -> dict:
#     response = requests.get("https://jsonplaceholder.typicode.com/posts")
#     if response.status_code == 200:
#         posts = response.json()
#         for post in posts:
#             if post["title"].lower() == title.lower():
#                 return post
#         return {"error": "Post not found"}
#     else:
#         return {"error": "Failed to fetch posts"}


def get_post_by_title(title: str):
    import requests
    posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    for post in posts:
        if post["title"] == title:
            return post
    return {"error": "Post not found"}
