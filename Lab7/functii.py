def reuniune(A,B):
    rez=set()
    for x in A:
        rez.add(x)
    for x in B:
        rez.add(x)
    return rez

def dif(A,B):
    rez=set()
    for x in A:
        if x not in B:
            rez.add(x)
    return rez

def xor(A,B):
    rez=set()
    rez.update(reuniune(dif(A,B),dif(B,A)))
    return rez

def disj(A,B):
    ok=True
    for x in A:
        if x in B:
            ok=False
    return ok

def prodcartezian(A,B):
    rez=list()
    for x in A:
        for y in B:
            rez.append(list([x,y]))
    return rez

def binar_set_U(U):
    n=0
    for x in U:
        n=n<<1 | 1
    return n

def binar_sets(U,V):
    n=0
    for x in U:
        if x in V:
            n=n<<1 | 1
        else:
            n=n<<1
    return n


def multime_putere(S, n):
    np = 1 << n  
    PS = []      
    for i in range(np):
        submultime = []
        for j in range(n):
            if (i >> j) & 1:
                submultime.append(S[j])
        PS.append(submultime)

    return PS