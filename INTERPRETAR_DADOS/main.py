import pandas as pd
# Import = chamar  biblioteca para o sistema
# O nome da biblioteca 
# "as" para apelidar a biblioteca

# df quer dizer data frame
df_alunos = pd.read_csv("alunos.csv", sep= ',', encoding='utf-8')
# pd.read_csv -  faz com que o pandas leia o arquivo csv para Python
# Caso o separador não é "," você arruma com o argumento sep = ''
# Caso ele não reconheça os operadores digitados, alteramos com o arg encoding = ''
print(df_alunos)

novo_aluno = { # Esse trecho cria um dicionário Python, onde cada chave corresponde ao nome de uma coluna do seu DataFrame.
    "Carimbo de data/hora":"17/11/2025 10:33:42",
    "nome":"Luiz", # Obs: os atributos do Dataframe, precisam estar de acordo com a original
    "cidade":"Iguape",
    "zona":"centro"
}

# Add o dado
df_alunos = pd.concat([df_alunos, pd.DataFrame([novo_aluno])], ignore_index=True)
# pd.DataFrame([novo_aluno]) → transforma esse dicionário em um DataFrame com uma linha.
# df_alunos = pd.concat([...], ignore_index=True) → adiciona essa nova linha ao DataFrame existente e reorganiza os índices.


# Salvar a info
df_alunos.to_csv("alunos.csv", index=False)
#df_alunos.to_csv("alunos.csv", index=False) → salva o DataFrame atualizado no arquivo CSV sem incluir a coluna de índices.

# DICIONÁRIO
# DATAFRAME: tabela de dados do pandas.
# CONCAT: É uma função do pandas que junta DataFrames.
# ignore_index=True: Um parâmetro do concat que diz: “Depois de juntar tudo, reorganize os índices do zero.”
# to_csv: Uma função do pandas que salva um DataFrame como arquivo CSV.
# index=False (no to_csv): Um parâmetro que diz: “Não inclua a coluna de índices no arquivo CSV.”
