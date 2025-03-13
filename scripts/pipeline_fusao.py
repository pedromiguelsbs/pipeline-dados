import json
import csv

path_json = 'raw_data/dados_empresaA.json'
path_csv = 'raw_data/dados_empresaB.csv'

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

#1) EXTRACT: lendo os dados
data_json = read_data(path_json, 'json')
data_csv = read_data(path_csv, 'csv')
#print(data_json[0])
#print(data_csv[0])


#2) TRANSFORM: padronizando colunas
columns_json = get_columns(data_json)
columns_csv = get_columns(data_csv)
#print(columns_json)
#print(columns_csv)
key_mapping = {'Nome do Item' :'Nome do Produto', 
                 'Classificação do Produto': 'Categoria do Produto', 
                 'Valor em Reais (R$)': 'Preço do Produto (R$)',
                 'Quantidade em Estoque': 'Quantidade em Estoque',
                 'Nome da Loja': 'Filial',
                 'Data da Venda': 'Data da Venda'}
new_data_csv = rename_columns(data_csv, key_mapping)
new_columns_csv = get_columns(new_data_csv)
#print(new_columns_csv)

#2.1) TRANSFORM: unindo os dados
combined_datas = join(data_json, new_data_csv)
#print(combined_datas[0])
#print(combined_datas[-1])

#2.2) TRANSFORM: Resolvendo a coluna 'Data da Venda' faltante no JSON


#3) Load