soma = 0
ultimo_numero = 0
penultimo_numero = 0
antepenultimo_numero = 0
cont_0 = 0
n = 0
cont_desconsiderados = 0
cont_considerados = 0
print("Bem vindo ao Zero Cancela")
while n >= 0:
    n = int(input("Digite um número (ou um número negativo para encerrar): "))
    if n > 0:
         cont_considerados += 1
    if n < 0:
        break
    elif n == 0:
            cont_desconsiderados+=1
            cont_0 += 1
            if cont_0 == 1:
                soma -= ultimo_numero
                ultimo_numero=penultimo_numero
                penultimo_numero=antepenultimo_numero
            elif cont_0 == 2:
                soma -= ultimo_numero
                ultimo_numero=penultimo_numero
            elif cont_0 == 3:
                soma -= ultimo_numero
            elif  cont_0 > 3:
                cont_desconsiderados-=1
                print(f"Só é permitido até 3 números consecutivos!!!")
    else:
        soma += n
        antepenultimo_numero = penultimo_numero
        penultimo_numero = ultimo_numero
        ultimo_numero = n
        cont_0= 0
print(f"Soma Total= {soma}")
print(f"Números Considerados= {cont_considerados - cont_desconsiderados}")
print(f"Números Desconsiderados= {cont_desconsiderados}")