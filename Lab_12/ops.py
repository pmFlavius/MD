import numpy as np
import sys

def citireMultime():
    multimi=list()
    for i in sys.stdin:
        s=set(map(int,i.split()))
        multimi.append(s)

    return multimi

def reflexivitate(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i==j:
                if A[i][j]==0:
                    return 0

    return 1

def simetrie(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j]==1 and A[j][i]!=1:
                if reflexivitate(A)==0:
                    return -1#asimetrie
                else:
                    return 0#antisimetrie
    return 1#simetrie

def tranzitivitate(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            for k in range(len(A)):
                if A[i][j]==1 and A[j][k]==1 and A[i][k]!=1:
                    return 0
    return 1

def reprezentareMat(relatie,n):
    M=np.zeros((n,n))
    M.astype(int)

    for elem in relatie:
        a=elem[0]
        b=elem[1]

        M[a-1][b-1]=1

    return M
#exemplu de graf Hasse
def Hasse():
    graf={
        'a':['b'],
        'b': ['c','d'],
        'c':[],
        'd':[]
    }

    #parcurgem fiecare nod din diagrama hasse
    for nod in graf:
        lista_nod = graf[nod]
        print("Nodul %c este acoperit de: " %nod,end=" ")

        #parcurgem fiecare nod care acopera nodul curent
        for nd in lista_nod:
            print(" %c " %nd,end=" ")

        print()
