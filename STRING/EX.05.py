'''Escreva um programa que leia a idade e o primeiro nome de
várias pessoas. Seu programa deve terminar quando uma
idade negativa for digitada. Ao terminar, seu programa deve
escrever o nome e a idade da pessoa mais jovem e mais
velha.
'''
idade=0
IV=0
while(idade>=0):
    nome=input("digite seu nome:")
    idade=int(input("digite sua idade:"))
    if(idade<0):
        break
    elif(idade>IV):
        NV=nome
        IV=idade
    elif(idade<IV):
        NN=nome
        IN=idade
print(f"Mais novo é {NN.title()},{IN} anos.")
print(f"Mais velho é {NV.title()},{IV} anos.")