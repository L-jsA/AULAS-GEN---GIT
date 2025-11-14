def menu(): # Define a função que exibe o menu principal.
    print("\nBem-vindo ao Protein-Cal-Gen")
    print("\nEscolha uma opção:")
    print("1 - Calcular proteínas")
    print("2 - Calcular IMC")
    print("Qualquer outro número - sair")

# Função para saber o objetivo do usuário
def menu_objetivo(): # Define a função que apresenta os objetivos do usuário.
    print("\nQual sua meta?")
    print("1 - Perder peso")
    print("2 - Manter peso")
    print("3 - Ganhar peso")

def calc_proteinas(peso, objetivo): # Define uma função que calcula proteínas com base no peso e objetivo.
    if objetivo == 1: # Verifica se o objetivo é perder peso.
        return peso * 2 # Retorna a quantidade recomendada de proteína para quem quer perder peso.
    elif objetivo == 2: # Verifica se o objetivo é manter o peso.
        return peso * 1.6 # Retorna a quantidade de proteína para manter o peso.
    elif objetivo == 3: # Verifica se o objetivo é ganhar peso.
        return peso * 1.8 # Retorna a quantidade de proteína para ganhar peso.
    else:
        return None
    # O comando None, é para não fazer nada

def  calc_imc(peso, altura): # Define uma função que calcula o IMC a partir do peso e altura.
    return peso / (altura **2) # Retorna o valor do IMC usando a fórmula peso dividido pela altura ao quadrado. Primeiro calcula a altura pela potência e depois a divisão

def imc(valor_imc): # Define uma função que classifica o IMC calculado.
    if valor_imc < 18.5: # Verifica se a pessoa está abaixo do peso.
        return "Abaixo do peso"
    elif valor_imc < 24.9: # Verifica se o IMC indica peso normal.
        return "Peso normal"
    elif valor_imc < 29.9: # Verifica se o IMC indica sobrepeso.
        return "Sobre peso"
    else: 
        return "Obesidade"

