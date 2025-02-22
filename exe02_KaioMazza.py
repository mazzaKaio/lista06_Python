# Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos, 
# solicite ao usuário para digitar um nome de produto e exiba a posição dele, 
# em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.

produtos = ("arroz", "feijao", "frango", "carne", "farofa", "amendoim", "laranja", "limao", "maracuja", "ovo")
confirmacao = "s"

print(produtos)

while confirmacao == "s":
    try:
        produtoDesejado = input("\nDigite o nome do produto desejado conforme a tupla acima: ").lower()
        posicaoProduto = produtos.index(produtoDesejado)
        print("O produto '{}' está na posição '{}' da tupla!".format(produtoDesejado, posicaoProduto))
        break
    except:
        print("\nProduto digitado não encontrado!")
        confirmacao = input("Deseja procurar novamente? [s/n]: ").lower()

confirmacao = "s"

while confirmacao == "s":
    try:
        indexProcurado = int(input("\nDigite um número entre 0 e 9: "))
        produtoIndex = produtos.__getitem__(indexProcurado)
        print("No index {} está o produto {}!".format(indexProcurado, produtoIndex))
        break
    except:
        print("\nIndex digitado não encontrado!")
        confirmacao = input("Deseja procurar novamente? [s/n]: ").lower()

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")