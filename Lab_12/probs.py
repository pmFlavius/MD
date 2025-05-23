from ops import *
import sys

def E1():
    R=list()
    for l in sys.stdin:
        a,b=map(int,l.split())
        R.append((a,b))
    A=reprezentareMat(R,4)
    if tranzitivitate(A)==1 and simetrie(A)==1 and reflexivitate(A)==1:
        print('\nRelatia este de echivalenta')
    else:
        print('\nRelatia nu este de echivalenta')
    if tranzitivitate(A)==0:
        print('\nNu este tranzitiva')
    if simetrie(A)!=1:
        print('\nNu este simetrica')
    if reflexivitate(A)==0:
        print('\nNu este reflexiva')
def O2():
    R=list()
    for l in sys.stdin:
        a,b=map(int,l.split())
        R.append((a,b))
    A=reprezentareMat(r,4)
    if tranzitivitate(A)==1 and simetrie(A)==0 and reflexivitate(A)==1:
        print('\nRelatia este de ordine partiala')
    else:
        print('\nRelatia nu este de ordine partiala')
    if tranzitivitate(A)==0:
        print('\nNu este tranzitiva')
    if simetrie(A)!=0:
        print('\nNu este antisimetrica')
    if reflexivitate(A)==0:
        print('\nNu este reflexiva')

def E2():
   S=citireMultime()
   for i in range(0,len(S)-1):
       for j in range(i+1,len(S)):
           print(S[i],S[j])
           Z=S[i].intersection(S[j])
           print(Z)
           if len(Z)!=0:
               print('Nu este partitie')
               return
   print('Este partitie')


def E4():
    A={1,2,4,5,7,11,13}
    R=list()
    for x in A:
        for y in A:
            if (x-y)%3==0 and x>=y:
                R.append((x,y))
    rel=reprezentareMat(R,13)
    if tranzitivitate(rel)==1 and reflexivitate(rel)==1 and simetrie(rel)==1:
        print('\nRelatia este de echivalenta')
    else:
        print('\nRelatia nu este de echivalenta') 
    if tranzitivitate(rel)==0:
        print('\nNu este tranzitiva')
    if simetrie(rel)!=1:
        print('\nNu este simetrica')
    if reflexivitate(rel)==0:
        print('\nNu este reflexiva')
