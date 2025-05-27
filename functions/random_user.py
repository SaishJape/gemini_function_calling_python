import requests

def get_random_user():
    try:
        response = requests.get("https://randomuser.me/api/")
        data = response.json()
        user = data['results'][0]
        name = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        country = user['location']['country']
        return {
            "name": name,
            "email": email,
            "country": country
        }
    except Exception as e:
        return {"error": str(e)}
