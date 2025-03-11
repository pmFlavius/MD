def implicatie(p,q):
    if p:
        return q
    else:
        return True

def xor(p,q):
    return (p+q)%2

def echiv(p,q):
    return p==q
