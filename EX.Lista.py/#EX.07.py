#EX.07
'''Construa um programa que leia dois números inteiros: a e b e uma lista com N valores inteiros (N fornecido pelo usuário).
O programa deverá imprimir quantos elementos da Lista pertencem ao intervalo [a;b]'''

lista=[]
perte=0
cont=0
a=int(input("Digite a:"))
b=int(input("Digite b:"))
quantn=int(input("Quantos num deseja por na lista:"))
for i in range(quantn):
    n=int(input("Digite um numero:"))
    if (n>a) and (n<b):
        cont+=1
    elif(n<a) and (n >b):
        cont+=1
print(f"A quantidade de numeros entre a e b é de: {cont}")