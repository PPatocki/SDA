'''
from yaml import load
from yaml import CLoader as Loader
with open('test.yml', 'r') as file_handler:
    root = load(file_handler, Loader=Loader)

for k, v in root.items():
    cls = v['class']
    name = v['name']
    hp = v['hp']
    armour = v['armour']
    skills = ', '.join(v['skills'])
    print(f'{k} class: {cls}, name: {name}, hp: {hp}, armour: {armour}, skills: {skills}')






for k, v in root.items():
    pass
for v in root.values():
    pass
for k in root.keys():
    pass
'''




l=[123, 56, 88, 44, 6]
a=0
for e in l:
    a+=e
print(a)
print(sum(l))
