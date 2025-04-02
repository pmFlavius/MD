from ops import *

def citireUnivers():
    Univers = []
    n=int(input('n= '))
    for i in range(0,n):
        Univers.append(int(input()))
    return Univers

def P7():#problema 7
    x=input('Alege subpunctul ')
    if x=='a':
        rez=True
        for a in (False,True):
            for b in (False,True):
                for c in (False,True):
                    expr1=implicatie(a,(b and c))
                    expr2= not b
                    if not implicatie(expr1 and expr2, not a):
                        rez=False
                        break
        if rez==False:
            print('Propozitia nu este echivalenta')
        else:
            print('Propozitia este echivalenta')
    elif x=='b':
        rez=True
        for s in (False,True):
            for r in (False,True):
                for p in (False,True):
                    for q in (False,True):
                        expr1=implicatie(s,r)
                        expr2=implicatie(p or q,not r)
                        expr3=implicatie(not s,implicatie(not q,r))
                        expr4=p
                        expr5=implicatie(expr1 and expr2 and expr3 and expr4,q)
                        if not expr5:
                            rez=False
                            break
        if rez==False:
            print('Propozitia nu este echivalenta')
        else:
            print('Propozitia este echivalenta')

def P1(Univers):#problema1
    x=input('Alege subpunctul ')
    if x=='a':
        LV = []
        rez = False
        for y in Univers:
            rez = rez or Q(5,y)
            if(Q(5,y)):
                LV.append(y)
        if rez:
            print('Rezultatul este %d pentru y =' %(rez))
            print(LV)
        else:
            print('Fals')
    elif x=='b':
        LV = [] 
        rez = False
        for x in Univers:
            rez = rez or Q(x,4)
            if(Q(x,4)):
                LV.append(x)
        if rez:
            print('Rezultatul este %d pentru x= '%(rez))
            print(LV)
        else:
            print('Fals')
    elif x=='c':
        LV = []
        rez1 = True
        for x in Univers:
            rez2=False
            for y in Univers:
                if(Q(x,y)):
                    rez2=True
                    LV.append((x,y))
                    break
            if not rez2:
                rez1=False
        if rez1:
            print(LV)
        else:
            print('Fals')
    elif x=='d':
        LV=[]
        rez2 = True
        for y in Univers:
            rez1 = False
            for x in Univers:
                if(Q(x,y)):
                    rez1=True
                    LV.append((x,y))
                    break
            if not rez1:
                rez2=False
        if rez2:
            print(LV)
        else:
            print('Fals')

    elif x=='e':
        LV=[]
        rez2=False
        for y in Univers:
            rez1=True
            temp=[]
            for x in Univers:
                if(not Q(x,y)):
                    rez1=False
                    break
                else:
                    temp.append((x,y))
            if rez1:
                LV.append(temp)
                rez2=True
        if rez2:
            print(LV)
        else:
            print('Fals')


def P2(U1,U2,U3):#problema2
    x=input('Alege subpunctul ')
    if x=='a':
       rez1=True
       LV = []
       for x in U1:
           rez2=False
           for y in U2:
               if(P(x,y)):
                   rez2=True
                   LV.append((x,y))
           if not rez2:
               rez1=False
       if rez1:
           print(LV)
       else:
           print('Fals')
    elif x=='d':
        rez1=True
        LV = [] 
        for x in U3:
            rez2=False
            for y in U3:
                if(R(x,y)):
                    rez2=True
                    LV.append((x,y))
            if not rez2:
                rez1=False
        if rez1:
            print(LV)
        else:
            print('Fals')

