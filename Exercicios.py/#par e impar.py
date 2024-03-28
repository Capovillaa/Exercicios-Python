#par e impar
Numero=int(input("Digite a quantidade de numeros a ser digitado:"))
i=1
QN=0
pares=0
impar=0
while (i<=Numero):
    QN=int(input("Digite os numeros:"))
    if(QN % 2 ==0):
        pares=pares + QN
    else:
        impar=impar+1
    i=i+1
print(f"A soma de todos os pares é {pares} e a quantidade de impar é {impar}")
