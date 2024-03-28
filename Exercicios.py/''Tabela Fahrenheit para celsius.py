'''Escreva um programa que, utilizando a fórmula que converte um
grau Fahrenheit em Celsius'''
for fa in range(30,51,2):
    Ce=(5/9)*(fa-32)
    print(f"Fahrenheit:{fa} em celsius:{Ce:.2f}")