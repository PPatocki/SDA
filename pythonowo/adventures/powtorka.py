'''
li.remove(2) usuwa pierwsza napotkana 2 w liscie
li2 = li[:] robi wierna kopie listy o innej referencji
del li[2] usuwa element o indeksie 2
li + other_li albo li.extend(other_li)

type((1)) to int
type((1,)) tuple
type(()) tuple

a, *b, c = (1, 2, 3, 4) a=1   b=[2, 3]  c=4

a, b = b, a  swapujemy

list(filled_dict.keys()) listuje klucze w slowniku
mozna wpisac .values()

'one' in filled_dict.keys()
1 in filled_dict.values()

filled_dict.get('one') => 1
filled_dict.get('four') => None zamiast errora jesli nie istnieje

filled_dict.get('four', 4) => da 4 jak nie ma 'four', domyslnie jest None

filled_dict.setdefault('five', 5) dziala tylko raz jak 'five' nie istnieje

filled_dict.update({'four': 4})
filled_dict['four'] = 4 dodaje do dicta

del filled_dict['one'] wywala klucz one

sety to zbiory unikalnych elementow

empty_set = set()
some_set = {1, 1, 2, 2, 3, 4} => {1, 2, 3, 4}
filled_set.add(5)

pamietac o continue i break

Exception jest klasa nadrzedna wszystkich errorow.
try:
    print(a) niezdefiniowana zmienna
except Exception as var:
    print(1) var lapie ten error
    
i wyswietli 1 bo lapie wszsytkiego rodzaju errory

################# CONTEXT MENAGER ####################

with open('average.py', 'r') as f:
    print(*f.readlines()[:2])

* rozpakowuje ten plik przez co wyswietli sie normalnie

with open('dupa.txt', 'r') as f:
    data = f.read()

for line in data:
    print(line)

/\ to jakbysmy chcieli szybko otworzyc i zamknac plik

class our_open:
    def __init__(self, file_name, read_attribute='r'):
        self.file_name = file_name
        self.read_attribute = read_attribute
  
    def __enter__(self):
        self.file = open(self.file_name, self.read_attribute)
        return self.file

    def __exit__(self, exc_val, exc_type, exc_tb):
        self.file.close()


with our_open('dupa.txt') as f:
    data = f.read()


print(data, f.closed)

/\ wlasnej roboty context menager

###############################################################################################


#### zadanko ###########

l = [1, 2, 3, 4, 5, 6, 7, 8, 8]


def dupa(l):
    l2=[]
    for e in l:
        l2.append(str(e))
    return l2


print(dupa(l))

########################

nl=[str(i) for i in l]

print(nl)

#############3##########

cl = list(map(str, l))
print(cl)

/\ to jest najlepsze. mapuje z typu na typ

dl = list(map(lambda x: str(x), l))
print(dl)

#############################################################################################
'''

l = [1, 45, 5, 2, 0, 1, 50, 2]



def equilibrium(l):
    i=0
    for e in l:
        if sum(l[:i+1]) == sum(l[i:]):
            break
        else:
            i+=1
            if i == len(l):
                i = None
    return i

#print(equilibrium(l))
    
l = [1, 2, 0, 2, 1, 1, 1, 1, 1]
print(equilibrium(l))
l = [1, 2, 0, 2, 1]
print(equilibrium(l))
l = [0]
print(equilibrium(l))
l = [1, 2, 0, 2, 1, 1]
print(equilibrium(l))









































































        
