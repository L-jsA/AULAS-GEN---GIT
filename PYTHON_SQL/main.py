from funcoes import *

# Integração de Mysql com scripts em Python
# Para usar Mysql com Python - mysql.connector



# Agora as opções do nosso sistema:
# mostrar tabela products;
# mostrar tabela customers;
# mostrar tabela orders;
# cadastrar products;
# cadastrar customers;
# cadastrar orders

while True:
    print('1 - Ver Produtos')
    print('2 - Ver Customers')
    print('3 - Ver Orders')
    print('4 - Cadastrar Products')
    print('1 - Cadastrar Customers')
    print('1 - Cadastrar Orders')

    opcao = input('informe a opção desejada')

    if opcao == '1':
        mostrar_tabela('products')
    elif opcao == '2':
        mostrar_tabela('customers')
    elif opcao == '3':
        mostrar_tabela('orders')
    elif opcao == '4':
        inserir_product()
    elif opcao == '5':
        inserir_customers()
    elif opcao == '6':
        inserir_orders()
    else:
        print('tchau')
        break

# Desligar o banco de dados ao finalizar o sistema
cursor.close()
conexao.close()
    
    


