import pandas as pd

funcionarios = pd.DataFrame({
    "id_funcionario":[1,2,3,4],
    "nome_funcionario":["Aline", "André", "Paulo", "Luiz"],
    "departamento_id": [100,200,300,400]
}) # criar uma tabela

departamento = pd.DataFrame({
    "departamento_id":[100,200,300,400],
    "nome_departamento":["TI", "RH", "Manutenção", "Financeiro"]
})

# Unir dados
funcionariosDepartamento = pd.merge(funcionarios, departamento, on="departamento_id" ) 
# une tabelas, mas precisa de três atributos: tabelas principal | tabela com os outros dados | campo referencial

print(funcionariosDepartamento)

# Chama a tabela unida[index com ela mesma e o campo que você quer] == 'condição'
print(funcionariosDepartamento[funcionariosDepartamento['nome_departamento'] == 'TI']) 