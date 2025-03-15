import json
import csv

class Dados:

    def __init__(self, path, type):
        self.__path = path
        self.__type = type
        self.__data = self.get_data()
        self.__columns = self.get_columns()
        self.__lenght = self.get_lenght()

    def __read_json(self):
        with open(self.__path, 'r') as file:
            data = json.load(file)
        return data

    def __read_csv(self):
        data = []
        with open(self.__path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                data.append(row)
        return data
    
    def rename_columns(self, key_mapping):
        new_data = []
        for old_dict in self.__data:
            new_dict = {}
            for old_key, value in old_dict.items():
                new_dict[key_mapping[old_key]] = value
            new_data.append(new_dict)
        #Atualiza os atributos modificados da instância
        self.__data = new_data
        self.__columns = self.get_columns()

    def join(data_a, data_b):
        combined_datas = []
        combined_datas.extend(data_a.__data)
        combined_datas.extend(data_b.__data)
        return Dados(combined_datas, 'list')
    
    #Resolvendo o problema da coluna faltante 'Data da Venda' no JSON
    def __standardize_columns(self):
        new_data = [self.__columns]
        for item in self.__data:
            row = []
            for column in self.__columns:
                row.append(item.get(column, 'Indisponível'))
            new_data.append(row)
        return new_data
    
    def save(self, path):
        data = self.__standardize_columns()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def get_data(self):
        if self.__type == 'json':
            data = self.__read_json()
        elif self.__type == 'csv':
            data = self.__read_csv()
        elif self.__type == 'list':
            data = self.__path
            self.__path = 'Lista em memória'
        return data            

    def get_columns(self):
        return list(self.__data[-1].keys())

    def get_lenght(self):
        return len(self.__data)