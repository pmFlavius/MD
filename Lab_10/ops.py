import numpy as np

def reprezentareMatriceala(relatie,n):
    M=np.zeros((n,n))
    M.astype(int)

    for elem in relatie:
        a=elem[0]
        b=elem[1]

        M[a-1][b-1]=1

    return M

def citireMatrice():
    A=list()
    n=int(input('Numarul de linii pentru matrice: '))
    for i in range(n):
        linie=list(map(int,input(f"Linia {i+1}:").split()))
        A.append(linie)
    return A


def MatOR(A,B):
    C=list()
    for i in range(len(A)):
        linie_rezultat=list()
        for j in range(len(A[i])):
                linie_rezultat.append(A[i][j] or B[i][j])

        C.append(linie_rezultat)

    return C
    
def MatAND(A,B):
    C=list()
    for i in range(len(A)):
        linie_rezultat=list()
        for j in range(len(A[i])):
                linie_rezultat.append(A[i][j] and B[i][j])

        C.append(linie_rezultat)

    return C


def MatProdBool(A, B):
    n, m = len(A), len(B[0])
    C = np.zeros((n, m), dtype=int)  

    for i in range(n):
        for j in range(m):
            val = 0
            for k in range(len(B)):
                val = val or (A[i][k] and B[k][j])
            C[i][j] = val
    return C