#EX.05
'''Elabore um programa que leia uma lista de no máximo 10 elementos reais, o programa deverá imprimir o maior e
segundo maior elemento e suas respectivas posições na lista'''
maior=0
lista=[]
for i in range(11):
    n=int(input("Digite um numero:"))
    lista.append(n)
print(max(lista))
lista.remove(max(lista))
print(max(lista))