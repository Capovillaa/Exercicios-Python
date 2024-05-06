#EX.01
livros = {}
inf_livro=[]
qnt_livros = int(input("Digite a Quantidade de livros que deseja cadastrar: "))
for i in range(qnt_livros):
    cod_livro = int(input("Qual o Código do livro: "))
    nome_obra = input("Qual o nome do livro: ")
    nome_autor = input("Digite o Nome do autor: ")
    preço = float(input("Digite o preço do livro: "))
    inf_livro.append(nome_obra.title())
    inf_livro.append(nome_autor.title())
    inf_livro.append(preço)
    livros[cod_livro] = inf_livro
    inf_livro=[]
print(livros)
print('-'*50)
menu=int(input("1: Busca Livro pelo Título\n2: Busca livro pelo Código\n3: Dados Livros preço superior a 50\nSelecione:"))
if(menu==1):
    cont=0
    busca_livro_nome=input("Digite o título do livro que deseja as informaçoes: ")
    for cod_livro, inf_livro in livros.items():
        if (inf_livro[0] == busca_livro_nome.title()):
            print(f"As informações são:\nCódigo: {cod_livro}\nNome: {inf_livro[0]}\nAutor: {inf_livro[1]}\nPreço: {inf_livro[2]}")
            cont+=1
    if cont == 0:
        print("Não Existe")
if(menu==2):
    busca_livro_cod = int(input("Digite o código do livro que deseja as informções: "))
    if busca_livro_cod in livros:
        print(f"As informações são:\n{livros[busca_livro_cod]}")
    else:
        print('Não existe')
if(menu==3):
    livros50=0
    for cod_livro, inf_livro in livros.items():
        if (inf_livro[2]> 50):
            print(f"As informações são:\nCódigo: {cod_livro}\nNome: {inf_livro[0]}\nAutor: {inf_livro[1]}\nPreço: {inf_livro[2]}")
            livros50+=1
    if(livros50==0):
        print("Não possui nenhum livro com valor maior que R$50")
