# Início do programa
def main():
    # Entrada de dados
    alimento = input("Digite um alimento: ").lower()

    # Decisões e saídas conforme o fluxograma
    if alimento == "arroz":
        print("Sim, o arroz é o melhor.") # imprime a informacao na tela
    elif alimento == "maçã":
        print("Maçãs não são a minha praia.") # imprime a informacao na tela
    else:
        print("Nunca ouvi falar!") # imprime a informacao na tela

# Fim do programa

if __name__ == "__main__":
    main()