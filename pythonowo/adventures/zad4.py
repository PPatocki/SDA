

l=[1, 2, 56, 0, 13, -3, 4, 0]

def index(l):
    x = l[0]
    w = 0
    result = 0
    for e in l:
        if e < x:
            x = e
            result = w
        w += 1
    return result

print(index(l))



def f(l):
    return l.index(min(l))
print(f(l))
