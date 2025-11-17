import pandas as pd

df_aviao = pd.read_csv("modelos.csv", sep= ';', encoding='utf-8')
print("Colunas encontradas no arquivo:")
print(list(df_aviao.columns))

novo_modelo = {
    "id": 8,
    "modelo": "Airbus A321neo",
    "companhia": "Azul",
    "capacidade": 240,
    "ano_fabricacao": 2021
}

df_aviao = pd.concat([df_aviao, pd.DataFrame([novo_modelo])], ignore_index=True)

df_aviao.to_csv("modelos.csv", index=False, sep=";")