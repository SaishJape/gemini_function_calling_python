import requests

def create_post(title: str, body: str, userId: int):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": userId
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            return response.json()
        else:
            return {"error": f"Failed with status {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}
