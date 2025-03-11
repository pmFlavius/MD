import functii as f

def main():
    x=int(input('x= '))
    nrcifre=f.calculnrcifre(x)
    pc=f.produscifre(x)
    print("Numarul cifrelor lui %d este %d"%(x,nrcifre))
    print("\nProdusul cifrelor lui %d este %d"%(x,pc))

if __name__=='__main__':
    main()
