import functii as f


def main():
    x=input("Introduceti numarul:\n")
    x=(int)(x)
    y=input("Introduceti puterea:\n")
    y=(int)(y)
    p=f.putere(x,y)
    print("%d la puterea %d este %d" %(x,y,p))

if __name__=='__main__':
    main()
