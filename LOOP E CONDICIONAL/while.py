# WHILE: comando de repetir
# WHILE == enquanto

# PRIMEIRA FORMA 
idade = 16

while idade < 18:
    print("Você é menor de idade")

# TATICA DO INCREMENTO
    idade = idade + 1 

# SEGUNDA FORMA
pergunta = input("Digite 'Sim' para sair")
# O simbolo != quer dizer diferente ou negar
while pergunta != "Sim":
    pergunta = input("Você digitou errado, digite mais uma vez")
    break # Comando break faz faz o sistema parar também

