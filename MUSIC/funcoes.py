# Para eu ler uma base de dados, preciso importar o módulo lê
import csv 

# Agora eu vou dizer onde está o arquivo que vou ler, digo o caminho (path) do arquivo

caminho_arquivo = "MUSIC/ASSETS/musicas(in).csv" # Define uma variável chamada caminho_arquivo para armazenar o caminho do arquivo CSV a ser lido.

# Sempre que eu quero criar uma função, eu coloco: a instrução "def" + "nome da função():"
def ler_musicas(): # Inicia a definição de uma função chamada ler_musicas.
    print("------ LISTA DE MÚSICAS ------") # Imprime uma linha de texto no console indicando o início da lista.

    try: # Inicia um bloco try para tratar possíveis erros (exceções) durante a execução do código.
        # O comando try serve para o sistema tentar executar uma ou mais instruções
        # Se der certo, ok, mas se não der certo, ele exibe uma mensagem de erro

        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_musica: # Abre o arquivo no modo de leitura ("r") com a codificação utf-8 e atribui o objeto do arquivo à variável arquivo_musica. Apenas cria a conexão com o arquivo no disco.
            # O caminho with open permite que eu abra algo, mas isso devo informar:
            # 1 - Onde está;
            # 2 - O modo abertura (ler - r; adicionar - a, reescrever - w)
            # 3 - NÃO OBRIGATÓRIO - Colocar como quer (codificar) e depois dá um apelido para essa instrução

            leitor = csv.reader(arquivo_musica) # Lê e interpreta o conteúdo do arquivo no formato CSV (separando as colunas).
            # Chamei um leitor para o sistema que lê csv e adicionei o método reader para ler o arquivo
            next(leitor)
            # O comando next é para pular a primeira linha do arquivo

            # Agora quero exibir linha por linha do que o leitor viu
            for cada_linha in leitor: # Inicia um loop que itera sobre cada linha do arquivo, exceto o cabeçalho
                if cada_linha: # Se cada linha: título, artista, ano e etc...
                    titulo,artista,ano,genero,duracao_segundos = cada_linha
                    # Tenho que falar todos os cabeçalhos do meu arquivo
                    print("Título", titulo, "Artista", artista, "Ano", ano, "Gênero", genero, "Duração em S", duracao_segundos)

    except FileNotFoundError: # Se o arquivo não for encontrado, dará uma mensagem de erro
        print("Error") 


            