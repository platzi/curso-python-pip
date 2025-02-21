import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    categories = r.json()
    print(categories)
    print(type(categories))
    
    for category in categories:
        title = category['name']
        print(title)