#vendedor de carros
CV=int(input("qual a quantidade de carros vendidos por este funcionario no mes:"))
TV=float(input("qual o total de vendas em reais:"))
salario= 1500 + 200*CV + TV*(5/100)
SB= 1500
Comissao= 200*CV
ADD5=TV*(5/100)
print(f"Salario base é de {SB}")
print(f"O número de carros vendidos é de {CV}")
print(f"O total de vendas em reais é de {TV:.3f}")
print(f"O total de comissao é de {Comissao}")
print(f"O adicional de 5% é igual a {ADD5:.3f}")
print(f"O salario final que irá ser recebido é de {salario:.3f}")