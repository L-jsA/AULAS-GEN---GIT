# O link da API sobre meteriologia se chama Endpoint
# Endpoint é o link para os métodos Get e Post
# Exemplo: https://api.open-meteo.com/v1/forecast

# Sempre que eu uso Api em Python, devo chamar a biblioteca de requisições pip install requests
# Biblioteca requests serve para fazer requisições HTTP
# Biblioteca matplotlib serve para criar gráficos

import requests 
import matplotlib.pyplot as plt #plot = exibir gráficos

# Criar uma função chamada de buscar_clima

def buscar_clima(latitude, longitude):
    # Sempre que usarmos a Api, temos que informar o endpoint
    endpoint= 'https://api.open-meteo.com/v1/forecast'
    # Informar os parâmetros para o sistema em formato de dicionário
    # Dicionário trabalha com chave:valor
    parametros= {
        # chave: valor,
        "latitude": latitude, # Colocamos a latitude e longitude nos parâmetros, pois o usuário terá que inserir
        "longitude": longitude,
        "hourly": "temperature_2m", # Diferente desses outros valores do dicionário que já virão do sistema. Essa seria a temperatura do local.
        #OBS: "hourly", não guarda apenas a temperatura, pode guardar outras coisas também, como o horário
        "timezone": "America/Sao_Paulo" # Informa fuso horário do local

    }
    resposta = requests.get(endpoint, params=parametros)
    # Sempre que queremos obter a resposta, usamos o comando requests.get para pegar os valores e colocamos os atributos:
    # requests.get(variavel_do_endpoint, params=dicionario_com_parametros)

    # Para o sitema usar o método post, para mostrar as informações
    dados = resposta.json()
    # O sistema transforma os dados em Json para poder manipular eles
    return dados

latitude = float(input("Informe a latitude"))
longitude= float(input("Informe a longitude"))

# Vamos começar a exibir informações para os usuários
dados = buscar_clima(latitude, longitude)

horas = dados["hourly"]["time"] # horário em que buscamos a informação
# Chamo a base de dados, informo o parâmetro e qual a variável que o parâmetro vai ter
temperatura=dados["hourly"]["temperature_2m"]

plt.plot(horas, temperatura)
#plt.plot cria um gráfico onde informo como parâmetro primeiro o eixo X e depois o eixo. Y
#plt.plot(eixo_x, eixo_y)
plt.title("TEMPERATURA POR HORA")

# Para ver o gráfico
plt.show()

