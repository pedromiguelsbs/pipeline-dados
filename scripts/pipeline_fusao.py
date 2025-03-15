from processamento import Dados

#EXTRACT
empresa_a = Dados('raw_data/dados_empresaA.json', 'json')
empresa_b = Dados('raw_data/dados_empresaB.csv', 'csv')

#TRANSFORM
key_mapping = {'Nome do Item' :'Nome do Produto', 
                 'Classificação do Produto': 'Categoria do Produto', 
                 'Valor em Reais (R$)': 'Preço do Produto (R$)',
                 'Quantidade em Estoque': 'Quantidade em Estoque',
                 'Nome da Loja': 'Filial',
                 'Data da Venda': 'Data da Venda'}
empresa_b.rename_columns(key_mapping) #padroniza as colunas
dados = Dados.join(empresa_a, empresa_b) #unifica dados

#LOAD
dados.save('processed_data/dados_combinados.csv')