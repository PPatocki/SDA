

a=3
b=5
'''
def pierdolnik(a,b):
    lista=[]
    for e in range(0,a):
        liswew=[]
        for f in range(0,b):
            liswew.append(f*e)
        lista.append(liswew)
    return lista


print(pierdolnik(a,b))
'''

def pierdolnik(a,b): return [[f*e for f in range(b)] for e in range(a)]
print(pierdolnik(a,b))
