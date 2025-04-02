from functii import *

def P1():
    A=set()
    B=set()
    print('\nIntroduceti elementele multimii A: ')
    for x in range(1,5):
        nr=int(input(''))
        A.add(nr)
    print('\nIntroduceti elementele multimii B: ')
    for x in range(1,7):
        nr=int(input(''))
        B.add(nr)
    C=reuniune(A,B)
    D1=dif(A,B)
    D2=dif(B,A)
    X=xor(A,B)
    Pc=prodcartezian(A,B)
    if disj(A,B):
        print("\nMultimile A si B sunt disjuncte")
    else:
        print("\nMultimile A si B nu sunt disjuncte")
    print("\nReuniunea dintre A si B este: ",C)
    print("\nDiferenta A-B este: ",D1)
    print("\nDiferenta B-A este: ",D2)
    print("\nDiferenta simetrica dintre A si B este: ",X)
    print("\nProdusul cartezian dintre A si B este: ",Pc)

def P4():
    U={1,2,3,4,5,6,7,8,9,10}
    A={2,4,6,8,10}
    B={1,2,3,4}
    uni=binar_set_U(U)
    nr1=binar_sets(U,A)
    nr2=binar_sets(U,B)
    print('\nA=', bin(nr1))
    print('\nB=', bin(nr2))
    conj=~ nr1
    reu=nr1 | nr2
    intersec=nr1&nr2
    xor=nr1^nr2
    print('\nConjugata lui A este: ',bin(conj))
    print('\nReuniunea A si B este: ',bin(reu))
    print('\nIntersectia A si B este: ',bin(intersec))
    print('\nDiferenta simetrica A si B este: ',bin(xor))
