import json
import csv

class Dados:

    def __init__(self, path, type):
        self.path = path
        self.type = type
        self.data = self.read_data()
        self.columns = self.get_columns()
        self.lenght = self.get_lenght()

    def read_json(self):
        with open(self.path, 'r') as file:
            data = json.load(file)
        return data

    def read_csv(self):
        data = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                data.append(row)
        return data

    def read_data(self):
        if self.type == 'json':
            data = self.read_json()
        elif self.type == 'csv':
            data = self.read_csv()
        elif self.type == 'list':
            data = self.path
            self.path = 'Lista em memória'
        return data
    
    def rename_columns(self, key_mapping):
        new_data = []
        for old_dict in self.data:
            new_dict = {}
            for old_key, value in old_dict.items():
                new_dict[key_mapping[old_key]] = value
            new_data.append(new_dict)
        #Atualiza os atributos modificados da instância
        self.data = new_data
        self.columns = self.get_columns()

    def join(data_a, data_b):
        combined_datas = []
        combined_datas.extend(data_a.data)
        combined_datas.extend(data_b.data)
        return Dados(combined_datas, 'list')
    
    #Resolvendo o problema da coluna faltante 'Data da Venda' no JSON
    def standardize_columns(self):
        new_data = [self.columns]
        for item in self.data:
            row = []
            for column in self.columns:
                row.append(item.get(column, 'Indisponível'))
            new_data.append(row)
        return new_data
    
    def save(self, path):
        data = self.standardize_columns()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def get_columns(self):
        return list(self.data[-1].keys())

    def get_lenght(self):
        return len(self.data)