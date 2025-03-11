def factorial(a:int)->int:
    if a==1:
        return 1
    else:
        return a*factorial(a-1)

def putere(n:int,k:int)->int:
    if k==0:
        return 1
    else:
        return n*putere(n,k-1)

def fibo(n:int)->int:
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fibo(n-2)+fibo(n-1)

def aranjamente(n:int,k:int)->int:
    if k==1:
        return n
    else:
        return (n-k+1)*aranjamente(n,k-1)

def citirelista(v:list)->int:
    n=0
    while True:
        try:
            x=int(input('x= '))
            v.append(x)
            n+=1
        except EOFError:
            break

    return n

def polinom(v:list,n:int,x:int)->int:
    if n==0:
        return v[0]
    else:
        return v[n]+x*polinom(v,n-1,x)

def produsscalar(a:list,b:list,n:int)->int:
    if n==0:
        return a[0]*b[0]
    else:
        return a[n]*b[n]+produsscalar(a,b,n-1)

def calculnrcifre(x:int)->int:
    if x==0:
        return 0;
    else:
        return 1+calculnrcifre(x//10)

def produscifre(x:int)->int:
    if x==0:
        return 1
    else:
        return (x%10)*produscifre(x//10)
