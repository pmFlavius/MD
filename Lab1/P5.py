import functii as f

def main():
   v=[] 
   n=int(input('n= '))
   for i in range(0,n):
       a=int(input())
       v.append(a)
   x=int(input('x= '))
   val=f.polinom(v,n-1,x)
   print("Valoarea polinomului in punctul %d este %d"%(x,val))

if __name__=='__main__':
    main()
