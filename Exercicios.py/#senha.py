#senha 
senha=1234
s=int(input("Digite a senha:"))
tentativa=1
while(tentativa<=3):
    if(s==senha):
        print("Acesso liberado")
        break
    s=int(input("Digite a senha novamente:"))
    tentativa=(tentativa+1)
    if(tentativa==3):
        break