from funcoes3 import *

while True: # Cria um loop infinito que só termina com o comando break
    menu() # Exibe o menu principal na tela.
    opcao = int(input("\nEscolha a opção"))

    if opcao == 1: # Verifica se o usuário escolheu a opção de calcular proteínas.
        menu_objetivo() # Exibe o menu com as metas do usuário.
        objetivo = int(input("\nQual seu objetivo?")) # Recebe o objetivo digitado e converte para inteiro.
        peso = float(input("\nQual peso(kg)")) # Solicita o peso do usuário e converte para número decimal.

        resultado_proteinas = float(calc_proteinas(peso, objetivo)) # Calcula a quantidade de proteínas usando a função importada.
        print("\nVocê precisa de", round(resultado_proteinas, 2)) # Mostra o resultado arredondado para duas casas decimais.
        # O comando round arredonta um número
        # Exemplo: 3,1415 - round(numero, 2) = 3,14
    elif opcao == 2: # Verifica se o usuário escolheu calcular o IMC.
        peso = float(input("\nQual peso(kg)?")) # Solicita o peso do usuário convertendo para decimal.
        altura = float(input("\nQual sua altura em metros?")) # Solicita a altura em metros e converte para decimal.

        resultado_imc = float(calc_imc(peso, altura)) # Calcula o IMC usando a função importada.
        print("\nSeu IMC é de", round(resultado_imc))

        classificacao = imc(resultado_imc)  # Chama a função imc
        print("Classificação:", classificacao)
    else: 
        print("Tchau")
        break


