from probs import *
import numpy as np
def main():
    x=int(input('Dati numarul problemei '))
    if x==7:
        P7()
    elif x==1:
        u1=[x for x in range(-2,3)]
        P1(u1)
    elif x==2:
        u1=[x for x in range(-10,11)]
        u2=[x for x in range(-100,101)]
        u3=np.arange(-10,10.1,0.1)
        P2(u1,u2,u3)



if __name__=='__main__':
    main()
