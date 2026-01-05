import pandas as pd
 
# =========================
# DataFrame de Funcionários
# =========================
funcionarios = pd.DataFrame({
    "id_funcionario": [1, 2, 3, 4, 5, 6],
    "nome_funcionario": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda"],
    "departamento_id": [10, 20, 10, 30, 20, 10],
    "cidade": ["São Paulo", "Rio de Janeiro", "São Paulo", "Curitiba", "Rio de Janeiro", "São Paulo"]
})
 
# =========================
# DataFrame de Departamentos
# =========================
departamentos = pd.DataFrame({
    "departamento_id": [10, 20, 30],
    "nome_departamento": ["Vendas", "Marketing", "TI"]
})
 
# =========================
# DataFrame de Vendas
# =========================
vendas = pd.DataFrame({
    "id_venda": [101, 102, 103, 104, 105, 106, 107, 108],
    "id_funcionario": [1, 2, 1, 3, 4, 5, 6, 1],
    "valor_venda": [500, 300, 700, 200, 900, 400, 650, 800],
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar", "Fev", "Mar"]
})
 
print("Funcionários:")
print(funcionarios)
 
print("\nDepartamentos:")
print(departamentos)
 
print("\nVendas:")
print(vendas)

func_dep = pd.merge(funcionarios, departamentos, on="departamento_id")
print(func_dep)

result_vend = pd.merge(func_dep, vendas, on="id_funcionario")
print(result_vend)

print(func_dep[func_dep['cidade'] == 'São Paulo']) 

# Filtro de múltiplas condições
print(result_vend[
    (result_vend['cidade'] == 'São Paulo') &
    (result_vend["valor_venda"] > 300)
])

# Agrupamento simples
# Venda x cidade
print(result_vend.groupby('cidade')['valor_venda'].sum())

# Venda x cidade: total | média | contagem
print(result_vend.groupby('cidade').agg(
    {'valor_venda':['sum', 'mean', 'count']}
))