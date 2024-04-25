#EX.04
'''Elabore um programa que leia um conjunto de vários valores inteiros e os coloque em 2 listas conforme forem pares ou 
ímpares (uma lista para números pares e outra lista para números ímpares). A leitura dos números é finalizada quando um número negativo é lido.'''
par=[]
impar=[]
n=0
while (n >=0):
    n=int(input("Digite um número:"))
    if(n<0):
        break
    elif (n % 2==0):
        par.append(n)
    else:
        impar.append(n)
print(f"LISTA PAR: {par}")
print(f"LISTA IMPAR: {impar}")