import requests 
import json


categorys_id = {'Автогума, диски, цепи': '(1d6f5bec-d49c-11e4-8586-002590aa75d3)', 'Аксесуари та інше': '(a5aa1e6f-d49b-11e4-8586-002590aa75d3)', 'Акумулятори': '(11722ecb-d49c-11e4-8586-002590aa75d3)'}

for category_name in categorys_id:
    
    base = requests.get('https://pitstop.rv.ua/s/catalog?Parent='+categorys_id[category_name])
    
    with open(category_name+'.json', 'wb') as file:
        file.write(base.content)

for category_name in categorys_id:
    
    with open(category_name+'.json') as file:
        list = json.load(file)
    
    for i in list:
        print(json.dumps(i, indent = 4, sort_keys=True))
        