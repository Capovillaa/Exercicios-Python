#EX que le 10 numeros e imprimi os dois maiores
maior1=0
maior2=0
for _ in range(10):
    N=int(input("Digite um numero:"))
    if(N>maior1):
        maior2=maior1
        maior1=N
    elif(N>maior2):
        maior2=N
print(f"Os DOIS MAIORES são {maior1} e {maior2}")
        