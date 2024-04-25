#EX.06
'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13
anos possuem altura inferior à média de altura desses alunos'''
soma=0
quant=0
idade=[]
altura=[]
for i in range (6):
    ida=int(input("DIGITE SUA IDADE:"))
    idade.append(ida)
    altu=int(input("DIGITE SUA ALTURA:"))
    soma+=altu
    altura.append(altu)
    media=soma/len(altura)
    if(ida>13) and (altu<media):
        quant+=1
print(f"{idade}")
print(altura)
print(media)
print(f"A quantidade de alunos que se encaixam na condição sao: {quant}")