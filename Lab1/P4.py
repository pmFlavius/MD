from functii import aranjamente

def main():
   n=input("Introduceti numarul de obiecte ")
   n=(int)(n)
   k=input("Introduceti numarul k ")
   k=(int)(k)
   a=aranjamente(n,k)
   print("Aranjamente de n luate cate k este egal cu %d"%a)

if __name__=='__main__':
    main()
