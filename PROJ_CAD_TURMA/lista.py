# Uma lista é uma "variável"que suporta muitos dados

frutas = []
# Quando eu coloco a lista apenas com [], eu estou dizendo que ela é vazia
print(frutas)

# O usuário pode add valor à lista, excluir a lista, ver a lista ou sair da lista

print("---- Bem-vindo ao varejão Gen-----")
print("\n Suas opções são: ")
print("\n 1 - add fruta")
print("\n 2 - excluir fruta")
print("\n 3 - ver lista")
print("\n 4 - sair")

escolha = int(input("Qual a opção desejada?"))
if escolha < 1 or escolha > 4:
    print("Escolha não reconhecida. Finalizando o sistema")
else: 
    while escolha >= 1 or escolha <= 4:
        # Caso 1 - add
        if escolha == 1:
            nova_fruta = input("\nQual fruta quer adicionar?")
            # Para adicionar um elemento na lista, eu devo chamar a lista e dar o atributo append, anexando assim o novo valor
            frutas.append(nova_fruta)
            print("Fruta", frutas[-1], "adicionada")
            escolha = int(input("\nQual a opção desejada?"))  # Volta nas opções 
        
        # Caso 2 - excluir
        elif escolha == 2:
            for posicao, cada_fruta in enumerate(frutas, start=1):  # Inicia um laço for que percorre a lista
                print(posicao, " - ", cada_fruta)
            print("\nAgora você pode excluir um produto")
            posicao_fruta = int(input("\nDigite a posição da fruta"))
            frutas.pop(posicao_fruta - 1)  # O número que o usuário digitou - 1
            print("\nFruta excluída com sucesso")
            escolha = int(input("\nQual a opção desejada?"))
        
        # Caso 3 - ver lista
        elif escolha == 3:
            for nome_frutas in frutas:
                print(nome_frutas)
            escolha = int(input("\nQual a opção desejada?"))
        
        # Caso 4 - sair
        elif escolha == 4:
            print("Tchau")
            break
