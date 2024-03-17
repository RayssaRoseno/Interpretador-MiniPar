from lexer import Lexer
from parser import Parser
from semantic_analyzer import SemanticAnalyzer

# Função para executar o teste 1
def executar_teste1():
    with open('C:/Users/rayss/Desktop/ParMini/teste1.mp', 'r') as file:
        codigo_teste = file.read()

    # Lexer
    lexer = Lexer(codigo_teste)
    tokens = lexer.tokenize()

    # Parser
    parser = Parser(tokens)
    ast = parser.programa_minipar()

    # Semantic Analyzer
    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.analyze(ast)

# Função para executar o teste 2
def executar_teste2():
    with open('C:/Users/rayss/Desktop/ParMini/teste2.mp', 'r') as file:
        codigo_teste = file.read()

    # Lexer
    lexer = Lexer(codigo_teste)
    tokens = lexer.tokenize()

    # Parser
    parser = Parser(tokens)
    ast = parser.programa_minipar()

    # Semantic Analyzer
    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.analyze(ast)

# Executar os testes
executar_teste1()
executar_teste2()
