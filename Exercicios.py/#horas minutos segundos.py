#horas minutos segundos
VS=int(input("Quantos segundos voce quer transformar:"))
VH= VS//3600
VS=VS%3600
VM=VS//60
VS=VS%60
print(f"Com essa quantidade obtemos {VH} horas, {VM} minutos, {VS} segundos")