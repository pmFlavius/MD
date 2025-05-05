from numpy import sqrt
from functools import reduce

def P1():
    D=list(range(-10,11))
    f=list(map(lambda x: 2*x,D))
    g=list(map(lambda x,y,z: x*x+3*y+5*z,D,D,D))
    print(f)
    print('\n')
    print(g)

def P2():
    D=(3.14159,-23.2381,-123.123,24,-96,36,64,-23,-74,-121,34)
    poz=filter(lambda x: x>0,D)
    f=tuple(map(lambda x: sqrt(x),poz))
    print(f)

def P3():
    v1=list()
    v2=list()
    n=int(input('Introduceti numarul de elemente al vectorului: '))
    print('Introduceti elementele vectorului I: ')
    for i in range(0,n):
        x=int(input())
        v1.append(x)
    print('Introduceti elementele vectorului II: ')
    for i in range(0,n):
        x=int(input())
        v2.append(x)
    suma=list(map(lambda x,y:x+y,v1,v2))
    print('Vectorul suma este ', suma)
    print('\n')
    p=list(map(lambda x,y:x*y,v1,v2))
    ps=reduce(lambda x,y:x+y,p)
    print('Produsul scalar este: ',ps)

def P4():
    v=list()
    n=int(input('Introduceti numarul de elemente al vectorului: '))
    print('Introduceti elementele vectorului: ')
    for i in range(0,n):
        x=int(input())
        v.append(x)
    #subpunctul 1
    poz=list(filter(lambda x: x>0,v))
    nule=list(filter(lambda x: x==0,v))
    neg=list(filter(lambda x: x<0,v))
    print('Numarul de elemente pozitive este: ',len(poz))
    print('\nNumarul de elemente negative este: ',len(neg))
    print('\nNumarul de elemente nule este: ',len(nule))
    print('\nElementele pozitive sunt: ',poz)
    print('\nElementele negative sunt: ',neg)
    #subpunctul 2
    maxim=reduce(lambda x,y: (x if x >= y else y),poz)
    print('\nMaximul elementelor pozitive este: ',maxim)
    suma=reduce(lambda x,y:x+y,neg)
    suma=-suma
    print('\nSuma valorilor absolute ale elementelor negative este: ',suma)
    norma=reduce(lambda x,y:x*x+y*y,v)
    norma=sqrt(norma)
    print('\nNorma euclidiana a vectorului citit este: ',norma)

def citirecuv(v:list):
    while True:
        try:
            x=input()
            v.append(x)
        except EOFError:
            print('\nAti terminat de introdus valorile! ')
            break
def P5():
    LW=list()
    citirecuv(LW)
    lungime=list(map(lambda x: len(x),LW))
    print('Lungimile cuvintelor din lista LW sunt: ',lungime)
    LW2=list(map(lambda x: str.upper(x),LW))
    print('\nCuvintele cu caracterele transformate in litere mari sunt: ',LW2)
    concat=reduce(lambda x,y: x+y,LW)
    print('\nCuvintele concatenate: ',concat)
    
