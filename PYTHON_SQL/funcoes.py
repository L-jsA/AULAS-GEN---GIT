import mysql.connector
import getpass # módulo para mascarar a senha

# Inserir no sistema as credenciais do banco de dados
user_host = input('informe o host')
user_user = input('informe o usuário')
user_password = getpass.getpass('informe a senha')
user_db = input('informe o banco de dados')

conexao = mysql.connector.connect(
    host = user_host,
    user = user_user,
    password = user_password,
    database = user_db

)

# Para executar a conexão com o banco de dados
cursor = conexao.cursor()


def mostrar_tabela(nome_tabela):
    print('tabela',nome_tabela)
    cursor.execute(f'select * from {nome_tabela}')
    # para coletar os resultados
    resultados = cursor.fetchall()

    # obter as colunas
    colunas = [desc[0] for desc in cursor.description]

    # exibir os nomes das colunas
    print(" | ".join(colunas))
    # id | nome | outras colunas |
    print('-'*50)

    # exibir os dados (linhas)
    for linha in resultados:
        print(" | ".join(str(item) for item in linha))
        # id | nome | outras colunas
        # | '1' | 'nome_cliente' | 'outros dados'

        # o comando description coleta os cabeçalhos de uma tabela
        # o comando fetchall coleta as linhas da tabela

def inserir_products():
    product_id = int(input('informe o id')) # placeholder(campo de digitar) - 1
    nome = input('informe o nome do produto') # placeholder 2
    price = float(input('ínforme preço do produto')) # placeholder 3

    # criar o script de sql
    sql = 'insert into products (productid, productname, price) values (%s,%s,%s)'
    # o %s representa um placeholder

    # executar o script
    cursor.execute(sql,(product_id, nome, price))

    # Confirmar o que fizemos
    conexao.commit()
    print('dados inseridos')



def inserir_customers():
    customer_id = int(input('informe o id')) # placeholder(campo de digitar) - 1
    customer_name = input('informe o nome do cliente') # placeholder 2
    

    # criar o script de sql
    sql = 'insert into customer (customerid, customername ) values (%s,%s)'
    # o %s representa um placeholder

    # executar o script
    cursor.execute(sql,(customer_id, customer_name))

    # Confirmar o que fizemos
    conexao.commit()
    print('dados inseridos')

def inserir_orders():
    order_id = int(input('informe o id')) # placeholder(campo de digitar) - 1
    order_date = input('informe a data do pedido(YYYY-MM-DD)') # placeholder 2
    customer_id = int(input('ínforme o id do pedido')) # placeholder 3
    product_id = int(input('ínforme o id do produto'))
    quantity = int(input('ínforme a quantidade do produto'))
    total = float(input('ínforme o total do produto'))

    # criar o script de sql
    sql = 'insert into orders (orderid, orderdate, customerid, productid, quantity, total) values (%s,%s,%s,%s,%s,%s)'
    # o %s representa um placeholder

    # executar o script
    cursor.execute(sql,(order_id, order_date, customer_id, product_id, quantity, total))

    # Confirmar o que fizemos
    conexao.commit()
    print('dados inseridos')

    