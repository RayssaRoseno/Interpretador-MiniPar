import os
from lexer import Lexer
from parser import Parser
from semantic_analyzer import SemanticAnalyzer

# Função para executar o teste 1
def executar_teste1():
    # Obter o diretório atual
    diretorio_atual = os.getcwd()
    # Alterar para o diretório onde os arquivos estão localizados
    os.chdir(diretorio_atual)

    with open('teste1.mp', 'r') as file:
        codigo_teste = file.read()

    # Restaurar o diretório atual após a conclusão
    os.chdir(diretorio_atual)

# Função para executar o teste 2
def executar_teste2():
    # Obter o diretório atual
    diretorio_atual = os.getcwd()
    # Alterar para o diretório onde os arquivos estão localizados
    os.chdir(diretorio_atual)

    with open('teste2.mp', 'r') as file:
        codigo_teste = file.read()

    # Restaurar o diretório atual após a conclusão
    os.chdir(diretorio_atual)

# Executar os testes
executar_teste1()
executar_teste2()
