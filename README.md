<h1 align="center">
    <img alt="Ícone Python" title="Ícone Python" src="assets/python-logo.png" width="120px" />
</h1>

<h2 align="center">Pipeline de dados: Combinando Python e Orientação a Objetos</h2>

<p align="center">
 <a href="https://www.linkedin.com/in/pedromiguelsbs/">
   <img alt="Criado por" src="https://img.shields.io/static/v1?label=Criado por&message=pedromiguelsbs&color=FFD34B&labelColor=000000">
 </a>
 <a href="https://github.com/pedromiguelsbs/pipeline-dados/blob/master/LICENSE">
   <img alt="License" src="https://img.shields.io/static/v1?label=License&message=MIT&color=FFD34B&labelColor=000000">
 </a>
</p>

<p align="center">
  <a href="#sobre">Sobre</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#conteúdo">Conteúdo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#como-usar-este-repositório">Como utilizar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contribuições">Contribuições</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#licença">Licença</a>
</p>

# Sobre 

Este repositório contém os arquivos e materiais do projeto de Construção de **Pipeline ETL** (Extract, Transform, Load). O objetivo é desenvolver um pipeline de dados eficiente para **unificar bases de duas empresas distintas**, garantindo consistência e qualidade dos dados.

## Conteúdo  

### Estruturando o Projeto
◻️ Organizando o projeto de Engenharia de dados

◻️ Uso de comandos Linux para criação de diretórios

◻️ Download de dados via wget

### Extraindo os Dados
◻️ Leitura de arquivos CSV e JSON

◻️ Uso da função open() para manipulação de arquivos

◻️ Escolha da estrutura adequada para armazenar os dados

◻️ Uso de readline() e readlines() para manipulação de texto

◻️ Leitura de arquivos com load() para JSON e DictReader() para CSV

### Transformando os Dados
◻️ Manipulação de dicionários: keys(), get(), items()

◻️ Alinhamento da estrutura de dados conforme requisitos do cliente

◻️ Renomeação de colunas

◻️ Junção de dados com extend()

◻️ Salvamento de dados transformados com DictWriter()

### Armazenando os Dados
◻️ Construção de estrutura de listas com for e get()

◻️ Salvamento de arquivos CSV com writer

### Criando funções
◻️ Transição da exploração de dados para a criação do pipeline

◻️ Refatoração do código com funções para extração, transformação e carregamento

◻️ Estruturação do código em etapas do pipeline ETL

### Refatorando com Programação Orientada a Objetos
◻️ Aplicação de conceitos de POO para modularização do pipeline

◻️ Transformação do pipeline de funções para uma classe

◻️ Criação de atributos e métodos

◻️ Refatoração do código para novas necessidades

◻️ Uso do pipeline de dados em scripts automatizados

## Como usar este repositório?  
1) Antes de executar o projeto, certifique-se de que você tem o seguinte pré-requisito instalado na sua máquina:

Python: Versão 3.8 ou superior.

Editor de código: Um editor como Visual Studio Code, PyCharm ou até mesmo o Jupyter Notebook (para explorar os notebooks)

2) O projeto está estruturado da seguinte forma:

`notebooks/`: Inclui o notebook 'exploracao.ipynb', que pode ser usado para explorar os dados.

`processed_data/`: Armazena os dados processados gerados no final do pipeline (dados_combinados.csv).

`raw_data/`: Contém os dados originais que serão processados.

`scripts/`: Armazena os arquivos principais para o processo de ETL

`pipeline_fusao.py`: Script principal que você deve executar para rodar o pipeline de fusão de dados e gerar os dados finais. 

`processamento.py`: Contém a classe Dados, que implementa a lógica orientada a objetos usada pelo pipeline_fusao.py.

## Contribuições
Se quiser sugerir melhorias ou compartilhar novos insights, fique à vontade para abrir uma _issue_ ou enviar um _pull request_.  

## Licença

Esse projeto está sob a licença MIT. Consulte o arquivo [LICENSE](https://github.com/pedromiguelsbs/pipeline-dados/blob/master/LICENSE) para mais detalhes.

---
