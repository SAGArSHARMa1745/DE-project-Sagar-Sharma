import requests

def get_data(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    try:
        res = requests.get(url)
        data = res.json()
        
        meaning = data[0]['meanings'][0]['definitions'][0]['definition']
        example = data[0]['meanings'][0]['definitions'][0].get('example', "No example")
        
        return meaning, example
    
    except:
        return "Not found", "No example"