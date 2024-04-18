'''Elabore um programa que leia nome, sexo e idade de um
usuário. Se sexo for feminino e idade menor que 25,
imprime o nome da pessoa e a palavra “ACEITA”, caso
contrário imprimir “NÃO ACEITA”'''











sexo=input('Sexo:')
idade=int(input("digite sua idade:"))
if (sexo.lower()=='feminino') or (sexo.lower()=='f') and (idade<25):
    print("ACEITA")
else:
    print("NÃO ACEITA")