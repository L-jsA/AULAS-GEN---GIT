# IF - É o comando "+SE" do excel
# Ou seja, ele é o comando de condições

# VERIFICAR IDADE
idade = int(input('Qual sua idade?'))

if idade >= 18: # Dentro desse bloco que se seguirá, o computador irá executar o que estamos pedindo
    # Indentação
    print("Você é maior de idade") 
else: 
    # O comando quer dizer "se não"
    print("Você é menor de idade")

# PROVA DE SOFTSKILLS
# Nota A = 9 ou 10
# Nota B = 8 ou 7
# Nota C = 6 ou 5
# Nota D = 4 ou menor

nota1 = int(input('Qual a nota 1?'))
nota2 = int(input('Qual a nota 2?'))
nota3 = int(input('Qual a nota 3?'))

media = (nota1+nota2+nota3)/3

if media > 10:
    print("Erro ao informar as notas")
elif media >= 9: # O comando elif é utilizado quando temos mais do que duas respostas possíveis para um elif
    print("Nota A")
elif media >= 7:
    print("Nota B")
elif media >= 5:
    print("Nota C")
else:
    print("Nota D")
