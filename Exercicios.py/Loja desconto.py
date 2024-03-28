#loja desconto valor etc...
PP=float(input("Qual o preço inicial do produto:"))
D=float(input("Qual o desconto deste produto:"))
PF=PP - (PP*(D/100))
print(f"O valor do produto sem o desconto era de R$ {PP:.2f} , porém possui um desconto de {D} %, saindo agora por apenas R$ {PF:.2f}")