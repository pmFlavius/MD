from functiigraf import *
from ops import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def P2():
    A={1,2,3,4,5,6};
    R=list();

    for a in A:
        for b in A:
            if b%a==0 and a<=b:
                R.append((a,b))
    print('Relatia R este: ',R)
    M=reprezentareMatriceala(R,len(A))
    print('\nForma matriceala a relatiei R este:\n ',M)
    V=creareListaNoduri(A)
    E=creareLaturi(R)
    G=creareGraf(V,E)
    desenareGraf(G)

def P3():
    A=citireMatrice()
    B=citireMatrice()
    C=MatOR(A,B)
    print('Jonctiunea A B este:\n',C)
    C=MatAND(A,B)
    print('Conjunctia A B este:\n',C)
    C=MatProdBool(A,B)
    print('Produsul boolean A B este:\n',C)

def P4():
    A=citireMatrice()
    B=citireMatrice()
    if len(A[0]) == len(B):
        C=MatProdBool(A,B)
        print('Produsul boolean A B este:\n',C)
    else:
        print('Dimensiuni gresite')
