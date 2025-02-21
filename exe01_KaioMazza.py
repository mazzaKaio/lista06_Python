#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.

paises = ("Brasil", "Venezuela", "Peru", "Republica Dominicana", "Espanha")
print(paises)
paisDesejado = input("Insira o nome de um país que foi mostrado acima: ").title()

try:
    print("\nO índice do país '{}' na tupa é: {}".format(paisDesejado, paises.index(paisDesejado)))
except:
    print("\nPaís não achado ou foi digitado errado!")