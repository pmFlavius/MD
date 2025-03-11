import functii as f

def main():
    n=int(input('n= '))
    a=[]
    b=[]
    for i in range (0,n):
       x=int(input())
       a.append(x)
    for i in range(0,n):
        x=int(input())
        b.append(x)
    ps=f.produsscalar(a,b,n-1)
    print("Produsul scalar dintre cei 2 vectori este %d"%ps)
if __name__=='__main__':
    main()
