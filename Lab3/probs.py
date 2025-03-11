from oplogic import *

def P1():#problema2
    x=int(input("Dati un numar de la 1 pana la 3: "))
    if x==1:
        print("%10s %10s %12s %10s %10s"%('p','q', 'expr1', 'expr2', 'expr'))
        for p in (False,True):
            for q in (False,True):
                expr1 = p and (not q)
                expr2 = not p or q
                expr = not(expr1 and expr2)
                print("%10d %10d %10d %10d %10d" %(p,q,expr1,expr2,expr))
    elif x==2:
        print("%10s %10s %10s %12s %10s %10s"%('p','q','r', 'expr1', 'expr2', 'expr'))
        for p in(False,True):
            for q in(False,True):
                for r in (False,True):
                    expr1=echiv(q,implicatie(r,not p))
                    expr2=echiv(implicatie(not q,p),r)
                    expr=expr1 or expr2
                    print("%10d %10d %10d %12d %10d %10d"%(p,q,r, expr1, expr2, expr))
    elif x==3:
        print("%10s %10s %10s %12s %10s %10s"%('p','q','r', 'expr1', 'expr2', 'expr'))
        for p in (False,True):
            for q in (False,True):
                for r in (False,True):
                    expr1=(p or q) and(not p or r)
                    expr2=q or r
                    expr=implicatie(expr1,expr2)
                    print("%10d %10d %10d %12d %10d %10d"%(p,q,r, expr1, expr2, expr))
                    
def P2():#problema3
    x=int(input("Introduceti un numar de la 1 la 2: "))
    if x==2:
        print("%10s %10s %12s %10s"%("p","q","expr1","expr2"))
        for p in (False,True):
            for q in (False,True):
                expr1=implicatie(p,q)
                expr2=implicatie(not p or q,p)
                if (expr1 and expr2) == True:
                    print("***%7d %10d %10d %10d" %(p,q,expr1,expr2))
                    pTemp=p
                    qTemp=q
                else:
                    print("%10d %10d %10d %10d" %(p,q,expr1,expr2))
        print()
        print('***')
        print("%10s %d" %("val(p)= ",pTemp))
        print("%10s %d" %("val(q)= ",qTemp))
    elif x==1:
        print("%10s %10s %12s %10s"%("p","q","expr1","expr2"))
        for p in (False,True):
            for q in (False,True):
                expr1=implicatie(p,p and q)
                expr2=(p or q)and not(p and q)
                if (expr1 and expr2) == True:
                    print("***%7d %10d %10d %10d" %(p,q,expr1,expr2))
                    pTemp=p
                    qTemp=q
                else:
                    print("%10d %10d %10d %10d" %(p,q,expr1,expr2))
        print()
        print('***')
        print("%10s %d" %("val(p)= ",pTemp))
        print("%10s %d" %("val(q)= ",qTemp))

def P3():#problema4
    #p:Stan este vinovat
    #q:Florin este vinovat
    #r:Bogdan este vinovat
    for p in (False,True):
        for q in(False,True):
            for r in (False,True):
                expr1=p and (not q)
                expr2=implicatie(r,q)
                expr3=not q and(p or q)
                if expr1 == expr2 and expr1==expr3:
                    pTemp=p
                    qTemp=q
                    rTemp=r
    if pTemp==True:
        print("\nStan este vinovat\n")
    if qTemp==True:
        print("\nFlorin este vinovat\n")
    if rTemp==True:
        print("\nBogdan este vinovat\n")

def P4():#problema6
    x=int(input("Introduceti un numar de la 1 la 2: "))
    if x==1:#iii)
        for p in (False,True):
            for q in (False,True):
                for r in (False,True):
                    expr1= p and (q or r)
                    expr2= (p and q) or (p and r)
                    expr= echiv(expr1,expr2)
                    if expr!=True:
                        print("Propozitia echivalenta(p and (q or r), (p and q) or (p and r) nu este tautologie")
                        return
        print("Propozitia echivalenta(p and (q or r), (p and q) or (p and r) este tautologie")
    elif x==2:#v)
        for p in (False,True):
            for q in (False,True):
                expr1=implicatie(p,q)
                expr=implicatie(p and expr1,q)
                if expr!=True:
                    print("Propozitia (p and(p->q))->q nu este tautologie")
                    return
        print("Propozitia (p and (p->q)) este tautologie")

def P5():#problema7
    x= int(input("Introduceti un numar de la 1 pana la 2: "))
    if x==1:#ii)
        taut=1
        cont=1
        for p in (False,True):
            for q in (False,True):
                for r in (False,True):
                    expr1=implicatie(p,q) and implicatie(q,r)
                    expr2=implicatie(p,r)
                    expr=implicatie(expr1,expr2)
                    if expr==True:
                        cont=0
                    elif expr==False:
                        taut=0
        if taut==False and cont==False:
            print("Propozitia ii) nu este nici tautologie nici contradictie")
        elif taut==False and cont==True:
            print("Propozitia ii) este contradictie")
        elif taut==True and cont==False:
            print("Propozitia ii) este tautologie")
    elif x==2:
        taut=1
        cont=1
        for a in (False,True):
            for b in (False,True):
                expr1=echiv(b,implicatie(b,a))
                expr=implicatie(expr1,a)
                if expr==True:
                    cont=0
                elif expr==False:
                    taut=0
        if taut==False and cont==False:
            print("Propozitia iii) nu este nici tautologie nici contradictie")
        elif taut==False and cont==True:
            print("Propozitia iii) este contradictie")
        elif taut==True and cont==False:
            print("Propozitia iii) este tautologie")

