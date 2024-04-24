#EX.03
'''Elabore um programa que leia e armazene 10 números reais, o programa deverá informar
• A média dos elementos
• O maior e o menor elemento
• A quantidade de números maiores que 29.
• Imprimir a lista lida'''
lista=[]
soman=0
maior29=0
for i in range(10):
    n=float(input("Digite um numero:"))
    lista.append(n)
    soman+=n
    if(n>29):
        maior29+=1
menor=min(lista)
maior=max(lista)
print(lista)
print(f"A media dos elementos é de {soman/10}")
print(f"maior = {maior} e menor = {menor}")
print(f"A quantidade de numeros maior que 29 é {maior29}")