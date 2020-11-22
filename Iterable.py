from domeniu.entitati import Student
class Lista():
    def __init__(self):
        self.list = []

    def append(self, value):
        return self.list.append(value)

    def __setitem__(self, key, value):
        self.list[key] = value

    def __getitem__(self, key):
        return self.list[key]

    def __delitem__(self, key):
        del self.list[key]

    def remove(self, element):
        self.list.remove(element)

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        return ListIterator(self)

class ListIterator:
    def __init__(self, lista):
        self.lista = lista
        self.pos = 0

    def __next__(self):
        if self.pos >= len(self.lista.list):
            raise StopIteration
        val = self.lista[self.pos]
        self.pos += 1
        return val

def itemComaparison(x: object(),y: object()):
    if x._s_id < y._s_id:
        return True
    return False
def gnomeSort(lista,comp):
    i=0
    while i < len(lista):
        if i!=0 and comp(lista[i], lista[i-1]):
            lista[i],lista[i-1] = lista[i-1],lista[i]
            i -= 1
        else:
            i += 1

def filter(x: object()):
    if x._s_id % 2 == 1:
        return True
    return False
def filterList(lista):
    res = []
    for elem in lista:
        if filter(elem):
            res.append(elem)
    return res