#EX.02
'''Construa um programa em Python que receba uma lista de 15 inteiros, via teclado e um número. O programa deve informar se
o número existe ou não na lista'''
lista=[]
for i in range(16):
    n=int(input("Digite um numero:"))
    lista.append(n)
n2=int(input("digite um numero para saber se ele esta na lista:"))
if (n2 in lista):
    print("O numero existe na lista!!")
else:
    print("O numero nao existe na lista!!")