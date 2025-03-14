import json
import csv

def read_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data

def read_csv(path):
    data = []
    with open(path, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            data.append(row)
    return data

def read_data(path, type):
    if type == 'json':
        data = read_json(path)
    elif type == 'csv':
        data = read_csv(path)
    return data

def get_columns(data):
    return list(data[0].keys())

def rename_columns(data, key_mapping):
    new_data = []
    for old_dict in data:
        new_dict = {}
        for old_key, value in old_dict.items():
            new_dict[key_mapping[old_key]] = value
        new_data.append(new_dict)
    return new_data

def join(data1, data2):
    combined_datas = []
    combined_datas.extend(data1)
    combined_datas.extend(data2)
    return combined_datas

def standardize_columns(old_data, column_pattern):
    new_data = [column_pattern]
    for item in list(old_data):
        row = []
        for column in column_pattern:
            row.append(item.get(column, 'Indisponível'))
        new_data.append(row)
    return new_data

def save_data(path, data):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)


#EXTRACT
#Lendo os dados
path_json = 'raw_data/dados_empresaA.json'
path_csv = 'raw_data/dados_empresaB.csv'
data_json = read_data(path_json, 'json')
data_csv = read_data(path_csv, 'csv')

#TRANSFORM
#Padronizando os nomes das colunas do CSV p/ igualar com as do JSON
columns_json = get_columns(data_json)
columns_csv = get_columns(data_csv)
key_mapping = {'Nome do Item' :'Nome do Produto', 
                 'Classificação do Produto': 'Categoria do Produto', 
                 'Valor em Reais (R$)': 'Preço do Produto (R$)',
                 'Quantidade em Estoque': 'Quantidade em Estoque',
                 'Nome da Loja': 'Filial',
                 'Data da Venda': 'Data da Venda'}
new_data_csv = rename_columns(data_csv, key_mapping)
new_columns_csv = get_columns(new_data_csv)
#Unindo os dados
combined_data = join(data_json, new_data_csv)

#LOAD
#Resolvendo o problema da coluna faltante 'Data da Venda' no JSON
new_combined_data = standardize_columns(combined_data, new_columns_csv)
#Salvando os dados
path = 'processed_data/dados_combinados.csv'
save_data(path, new_combined_data)
print(f"Dados salvos em: {path}")