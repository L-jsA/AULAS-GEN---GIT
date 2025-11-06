# ABERTURA DO SISTEMA
print("Bem vindo a aula de Python, vamos aprender a trabalhar com variáveis")

nome_usuario = "Luana"
# Essa memória é do tipo...
senha_usuario = "123"
# Essa méoria é do tipo...

print("usuario", nome_usuario, "senha", senha_usuario)

# ATIVIDADE 1 - CRIANDO UMA PERSONA
print("Vamos criar uma persona?")

# CRIAR AS VARIÁVEIS
nome_persona = input("Informe o nome da persona") # Se eu uso o input apenas, a informação armazena na variável é um texto

idade_persona = int(input("Qual sua idade?")) # Ao combinar o comando int com o comando input - int(input()) - eu armazeno em resposta como um número inteiro 

altura_persona = float(input("Informe sua altura"))
# Ao combinar float com input - float(input()) - armazenamos a resposta com um número decimal

# TRÊS TIPOS DE DADOS (DATA TYPES)
# STR - Para textos
# INT - Para números inteiros
# FLOAT - Para números decimais

print("Olá! ", nome_persona, " sua idade é: ", idade_persona, " e sua altura é: ", altura_persona)

# CÓDIGO EXTRA
falta_100 = 100 - idade_persona

print("Faltam", falta_100, "Para chegar aos 100 anos de idade") # Nome da pessoa, faltam XX anos

print(type(falta_100)) # Mostra o tipo de dados. Nesse caso, seria do tipo inteiro

falta_100_text = str(falta_100) # Converte o dado de inteiro para string(texto)
print(type(falta_100_text))

# LISTA: Basicamente é uma variável que suporta muitos valores

# PRIMEIRO MODO
aluno = ["Pedro J", "Rhayna L", "Daniel", "Luiz"]
print(aluno) # Irá exibir todos os elementos da lista "äluno"

# SEGUNDO NOME
print(aluno[2]) # Só pega um elemento da lista. No caso a posição 2 é o Daniel

# TERCEIRO MODO
print(aluno[-1]) # Chama o último número da lista. No caso a posição -1 é o Luiz

# QUARTO MODO
pessoas = {"nome":"Luiz", "idade":31, "cidade":"Iguape"} # Outra forma de listas, só que com chaves
print(pessoas)

# Para ordenar a lista
print(aluno.sort())


