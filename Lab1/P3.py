from functii import fibo

def main():
    x=input("Introduceti numarul")
    x=(int)(x)
    f=fibo(x)
    print("Al %d numar din sirul lui fibonacci este %d"%(x,f))

if __name__=='__main__':
    main()
