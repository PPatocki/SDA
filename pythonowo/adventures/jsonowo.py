import json
'''
a = json.loads(
    """
    [{
        "name": "doop'pa"
    },{
        "name": "Legolas"
    }]
    """
)
'''
with open('dupa.json') as file_handler:
    x = file_handler.read()
a = json.loads(x)
'''
print(a)
print(a['name'])
'''
'''
Class: Warrior, name: Doop'pa, hp: 10, strength: 42, armour: 5
'''
#obj a[0]
def pr(obj):
    x = obj['character_class']['name']
    y = obj['name']
    z = obj['hp']
    q = obj['character_class']['strength']
    w = obj['armour']

for element in a:
    print(pr(element))


'''
print(f'Class: {x}, name: {y}, hp: {z}, strength: {q}, armour: {w}')
'''
