import requests

def translate_text(text: str) -> str:
    """
    Translate text using the AIBIT Translator API.
    
    Args:
        text (str): The text to translate.
        
    Returns:
        str: The translated text.
    """
    
    url = "https://aibit-translator.p.rapidapi.com/api/v1/translator/text"
    
    headers = {
        "X-RapidAPI-Key": "82aa2b1fbbmsh4ef73325297a2f5p1bea3bjsnba30f3e7d41a",
        "x-aibit-key": "5cf048c0-13ba-11ee-a37b-d799f0284f13",
        "Content-Type": "application/json"
    }
    
    payload = {
        "from": "es",
        "to": "en",
        "text": text
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()
        return response_json.get("trans", "Translation not found")
    else:
        raise Exception(f"Translation failed with status code: {response.status_code}, Response: {response.text}")