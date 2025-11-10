# TERCEIRA FORMA
palavra = input("Digite uma palavra tudo em maisculo") # Aqui o usuário coloca a palavra em maisculo

print(palavra.lower()) # Aqui ele transforma em minusculo 
# O comando lower() deixa todo o conteúdo da variável minisculo

palavra2 = input("Para finalizar o sistema") # inserimos uma nova palavra

while palavra2.lower() == "sair" or palavra2.lower() == "finalizar":
    print("Sistema finalizado")
    # while cria um loop, ou seja, um bloco de código que repete enquanto a condição for verdadeira.
    # palavra2.lower() transforma o que o usuário digitou em minúsculas.
    # A condição == "sair" or == "finalizar" verifica se o usuário digitou "sair" ou "finalizar".
    # Enquanto isso for verdadeiro, o loop continua rodando.
print("Você digitou errado, mas acabou o exemplo")