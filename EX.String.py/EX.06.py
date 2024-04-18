S=input('Digite uma frase:')
Semespaço=(S.replace(" ",""))#defini essa variavel para que seja possivel verificar um palindromo em frases pois se contar o espaço obviamente n funciona
if(Semespaço.lower() == Semespaço.lower()[::-1]):#aqui pode ser == ou IN tbm funcionaria
    print(f"A string {S.title()} é um Palíndromo")
else:
    print("Não é um palíndromo")