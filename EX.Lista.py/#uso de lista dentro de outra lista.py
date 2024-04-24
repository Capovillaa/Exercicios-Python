#uso de lista dentro de outra lista
pessoa=[]
n=int(input("Quantas pessoas deseja cadastrar:"))
for i in range(n):
    dados=[]
    nome=input("digite seu nome completo:")
    nome.title()
    estado_civ=input("Qual seu estado civil:")
    estado_civ.capitalize()
    pfilhos=input("possui filhos(Digite S/N):")
    while (pfilhos.lower()!='n') and (pfilhos.lower()!='s'):
        print("Digite S ou N")        
        pfilhos=input("possui filhos(Digite S/N):")
    qnt_f=0
    filhos=[]
    if (pfilhos.lower()=='s'):
        qnt_f=int(input("Quantos filhos:"))
        for k in range(qnt_f):
            print(f"filhos {k+1}- ",end='')
            aux=int(input("Idade:"))
            filhos.append(aux)
    else:
        filhos.append('Não possui filhos')
    dados.append(nome.title())
    dados.append(estado_civ.capitalize())    
    dados.append(qnt_f)
    dados.append(filhos)
    pessoa.append(dados)
print(pessoa)