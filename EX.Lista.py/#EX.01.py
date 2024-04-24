#EX.01
'''Construa um programa em Python que receba uma lista de 10 inteiros, via teclado e imprima toda a lista na mesma linha'''
lista=[]
for i in range(11):
    n=int(input("digite um numero:"))
    lista.append(n)
print(lista)