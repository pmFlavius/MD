import functii as f

def main():
    x=input("Introduceti numarul ")
    x=(int)(x)
    nr=f.factorial(x)
    print("Factorialul numarului %d este %d "%(x,nr))

if __name__=='__main__':
    main()
