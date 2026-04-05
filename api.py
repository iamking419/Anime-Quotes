import requests

api = "https://api.animechan.io/v1/quotes/random"

def get_api():
    try:
        res = requests.get(api)
        res.raise_for_status()  # throw if HTTP error
        data = res.json()
        quote_text = data['data']['content']
        anime_name = data['data']['anime']['name']
        character_name = data['data']['character']['name']
        return f"{character_name} ({anime_name}): {quote_text}"
    except Exception as e:
        return f"Error fetching quote: {e}"

print(get_api())