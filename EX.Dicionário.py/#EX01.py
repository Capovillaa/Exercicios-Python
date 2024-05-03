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
busca_livro_nome=input("Digite o nome do livro que deseja as informaçoes: ")
for cod_livro,inf_livro in livros.items():
    if inf_livro[0]== busca_livro_nome.title():
        print(f"As informações são:\nCódigo: {cod_livro}\nNome: {inf_livro[0]}\nAutor: {inf_livro[1]}\nPreço: {inf_livro[2]}")
    else:
        print("Não existe")
busca_livro_cod = int(input("Digite o código do livro que deseja as informções: "))
print(f"As informações são:\n{livros[busca_livro_cod]}")
