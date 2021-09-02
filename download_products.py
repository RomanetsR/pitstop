import requests 


categories = {
    'Автогума, диски, цепи': '(1d6f5bec-d49c-11e4-8586-002590aa75d3)', 
    'Аксесуари та інше': '(a5aa1e6f-d49b-11e4-8586-002590aa75d3)', 
    'Акумулятори': '(11722ecb-d49c-11e4-8586-002590aa75d3)'
    }

for name in categories:
    
    base = requests.get('https://pitstop.rv.ua/s/catalog?Parent='+categories[name])
    
    with open(name+'.json', 'wb') as file:
        file.write(base.content)
