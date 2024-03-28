#simulaçao de caixa
VC=int(input("Qual o valor da compra:"))
VP=int(input("Qual o valor pago pelo cliente:"))
T=VP-VC
print(f"O troco é {T}")
cedula=20
Tced = 0
while True:
    if T >= cedula:
        T-= cedula
        Tced += 1
    else:
      if Tced > 0:
       print(f"O total é de {Tced} cedulas de R${cedula}")
      if  cedula == 20:
           cedula = 10 
      elif cedula ==10:
            cedula = 5
      elif cedula == 5:
            cedula = 1
      Tced = 0
      if T == 0:
             break