# Autor: Luana
# Projeto: FizzBuzz
# Versão: v1.x.y
# Descrição O Fizzbuzz é um exercício que imprime número de 1 a 100
# Sempre que é multiplicdo de 3, ele imprime "Fizz"
# Sempre que é múltiplo de 5, ele imprime "Buzz"
# E se for, multiplo de 3 e 5, ele imprime "FizzBuzz"

numero = 1

# Caso usando While
while numero <= 100: # Repita esse bloco enquanto numero for menor ou igual a 100
    if numero % 3 == 0: # significa que o número é divisível por 3
        if numero % 5 == 0: # Se o número é divisível por 3, e também é divisível por 5.
            print("FizzBuzz")
        else:
            print("Fizz") # Esse else pertence ao primeiro if. Então, se o número for divisível por 3, mas não por 5, ele imprime apenas:
    elif numero % 5 == 0: # Se o número não for múltiplo de 3, o programa verifica se é múltiplo de 5.
        print("Buzz") # Ele irá imprimir só Buzz
    else:
        print(numero) # Se não for nenhuma das condições, ele irá imprimir o número inteiro
    numero = numero + 1 

# Caso usando For

# Para cada elemento entre 1 e 100

for i in range(1,101): # serve para gerar uma sequência de números inteiros. Número onde a contagem para (⚠️ o valor final não é incluído)
    # Se o resto da divisão de 1 por 3
    # For zero e o resto da divisão 
    # De i por 5 também for zero faça 
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Se fosse um número aleatório
fizzbuzz = int(input("informe um número"))

if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print("Fizzbuzz")
elif fizzbuzz % 3 == 0:
    print("Fizz")
elif fizzbuzz % 5 == 0:
    print("Buzz")
else: 
    print(fizzbuzz)