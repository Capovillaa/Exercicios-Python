#EX5
A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))
D=int(input("D:"))
E=int(input("E:"))
F=int(input("F:"))
if((A*E)-(B*D)>=0):
    x=(C*E)-(B*F)/(A*E)-(B*D)
    y=(A*F)-(C*D)/(A*E)-(B*D)
    print(f"O valor de x é {x} e o de y é {y}")
else:
    print("O sistema nao tem soluçao")
