"""
Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma lista. 
Depois de inserir os três nomes, pergunte se deseja adicionar outro. Se o fizer, permita que adicione mais nomes até responder "não". 
Quando ele responder "não", mostre quantas pessoas ele convidou para a festa, uma vez que o usuário tenha completado sua lista de nomes, 
exiba a lista completa e peça que ele digite um dos nomes da lista. Exiba a posição desse nome na lista. 
Pergunte ao usuário se ele ainda deseja que essa pessoa venha à festa. Se ele responder "não", exclua essa entrada da lista e exiba a lista novamente.
"""

convidados = []

for i in range(3):
    nomeConvidado = input("Digite o nome do {}º convidado: ".format(i+1))
    convidados.append(nomeConvidado)

confirmacao = input("Agora, você deseja adicionar mais algúem a sua lista? [s/n]: ").lower()

while confirmacao[0] == "s":
    nomeConvidado = input("Insira o nome do novo convidado: ")
    convidados.append(nomeConvidado)
    confirmacao = input("\nAgora, você deseja adicionar mais algúem a sua lista? [sim/s, nao/n]: ").lower()

print("\nVocê convidou {} pessoas para sua festa!\nLista de convidados: {}".format(len(convidados), convidados))

