from funcoes2 import * # Importa todas as funções do arquivo funcoes2.
# * = all = tudo

def menu(): # Define uma função chamada menu.
    print("Gen - Calc")
    print("1 - somar")
    print("2 - subtrair")
    print("3 - multiplicar")
    print("4 - dividir")
    print("5 - potência")
    print("6 - raiz")
    print("Qualquer outro digito - sair")

# Vou criar a função principal de todo sistema

if __name__ == "__main__": # Garante que o código abaixo só execute se o arquivo for rodado diretamente.
# O if _name_ == "_main_": garante que o código só rode quando você executar o main.py

    menu() # Chama a função que exibe o menu.
    opcao = input("Escolha uma opção") # Pede ao usuário para escolher uma operação.

    num1 = float(input("Digite o número 1")) # Solicita o primeiro número e converte para float.
    num2 = float(input("Digite o numero 2")) # Solicita o segundo número e converte para float.

    if opcao == "1": # Se a opção for 1, executa a função soma e mostra o resultado.
        print(soma(num1, num2))
    elif opcao == "2": # Se a opção for 2, executa a função subtração e mostra o resultado.
        print(subtracao(num1, num2))
    elif opcao == "3": # Se a opção for 3, executa a função multiplicação e mostra o resultado.
        print(multiplicacao(num1, num2))
    elif opcao == "4": # Se a opção for 4, executa a função divisão e mostra o resultado.
        print(divisao(num1, num2))
    elif opcao == "5": # Se a opção for 5, executa a função potência e mostra o resultado.
        print(potencia(num1, num2))
    elif opcao == "6": # Se a opção for 6, executa a função raiz e mostra o resultado.
        print(raiz(num1, num2))
    else:
        print("Tchau") # Se nenhuma opção válida for escolhida, o programa encerra com uma despedida


