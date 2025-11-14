def soma(num1, num2): # Parâmetros () são valores que uma função recebe para conseguir executar uma tarefa específica.
    return num1 + num2
# O return é um comando parecido com o print
# Ele retorna a informação de uma função

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro, não posso dividir por 0"
    return num1 / num2

def potencia(num1, num2):
    return num1 ** num2

def raiz(num1, num2):
    return num1 ** (1/num2)