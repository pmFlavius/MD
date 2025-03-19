#operatori
def xor(p,q):
    return (p+q)%2

def implicatie(p,q):
    return not p or q

def echiv(p,q):
    return p==q

#predicateexercitii
def Q(x,y):
    r=((x+y)==(x-y))
    return r

def P(x,y):
    r=((x*x)==y)
    return r

def R(x,y):
    r=((x*y)==1.0)
    return r

