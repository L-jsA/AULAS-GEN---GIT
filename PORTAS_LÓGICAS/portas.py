# As portas lógicas sào divididas em três principais:
# NOT: negar alguma informação (não)
# OR: porta para uma condição (ou)
# AND: porta de condição (e)

# PRIMEIRO MODO

a = True
b = False

# Seja a variável a ou b quaisquer, podemos ter vários resultados
print("Not A", not a) 
# Negou o a, pois ele era verdadeiro
# Em alguns momentos eu posso usar o operador != para falar que é diferente

# SEGUNDO MODO

# PORTA OR
print("a ou b", a or b)

# TERCEIRO MODO

# PORTA DO AND
print("a e b", a and b)

# PRIMEIRO EXEMPLO - AND

idade = 16 # Cria uma variável chamada idade e define o valor inicial como 16.
carteira = False # Cria uma variável carteira e define como False, indicando que a pessoa ainda não tem carteira de motorista.

# enquanto for menor de idade E nao tiver carteira o sistema pergunta
# se eu fiz aniversario e se eu tirei a carteira
# quando eu tiver idade + carteira ele fala que eu posso dirigir
while idade < 18 or carteira == False: # Inicia um laço de repetição (while) que vai continuar enquanto a pessoa for menor de 18 OU não tiver carteira.
    pergunta_aniversario = input('Você já fez aniversário?')
    if pergunta_aniversario.lower() == 'sim': # Verifica se a resposta do usuário (convertida para minúscula) é "sim".
        idade = idade +1 # Se a pessoa respondeu "sim", soma 1 à idade.
        print("Parabéns! Entao vcoê tem", idade)
    pergunta_carteira = input('Você tirou carta?')
    if pergunta_carteira.lower() == "sim": # Se a resposta for "sim", a variável carteira passa a ser True, indicando que a pessoa agora tem carteira.
        carteira = True
    else:
        carteira = False # Se a resposta não for "sim", a variável continua False.

print("Pode dirigir")


