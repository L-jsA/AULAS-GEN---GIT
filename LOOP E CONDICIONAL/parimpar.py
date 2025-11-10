# Quais são os operadores matemáticos da informática
# Soma (+)
# Subtração (-)
# Multiplicação (*)
# Divisão (/)
# Resto (%)

# JOGO DO PAR OU ÍMPAR: Criar o jogo do par ou impar usando IF
# REGRAS
# 1. Perguntar ao usuário dois números
# 2. Somar esses dois números
# 3. Aplicar operação % para descobrir o resto
# 4. Se o resto for 0 é par
# 5. Se não, é impar

numero1 = int(input("Digite o primeiro número"))
numero2 = int(input("Digite o segundo número"))

resultado = numero1 + numero2

resto = resultado % 2

if resto == 0:
    print("O resultado é par")
else:
    print("O resultado é impar. E o número é:", resto)
    

