class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo  # Tipo do token (e.g., IDENTIFICADOR, NUMERO, etc.)
        self.valor = valor  # Valor associado ao token (e.g., o nome de um identificador, o valor de um número, etc.)

class Lexer:
    def __init__(self, codigo):
        self.codigo = codigo  # O código-fonte a ser tokenizado
        self.posicao = 0  # A posição atual no código-fonte
        self.tokens = []  # Lista de tokens identificados

    def tokenize(self):
        while self.posicao < len(self.codigo):  # Enquanto houver caracteres para processar no código-fonte
            char_atual = self.codigo[self.posicao]  # Obtém o caractere atual

            if char_atual.isspace():  # Se for um caractere de espaço em branco, ignora
                self.posicao += 1
            elif char_atual.isalpha():  # Se for uma letra, identifica um identificador
                token = self.obter_identificador()
                self.tokens.append(token)
            elif char_atual.isdigit():  # Se for um dígito, identifica um número
                token = self.obter_numero()
                self.tokens.append(token)
            elif char_atual == '#':  # Se for um caractere de comentário, ignora o restante da linha
                self.ignorar_comentario()
            # Identificação de caracteres especiais
            elif char_atual == '{':
                token = Token('ABRE_CHAVE', char_atual)
                self.tokens.append(token)
                self.posicao += 1
            elif char_atual == '}':
                token = Token('FECHA_CHAVE', char_atual)
                self.tokens.append(token)
                self.posicao += 1
            elif char_atual == ';':
                token = Token('PONTO_VIRGULA', char_atual)
                self.tokens.append(token)
                self.posicao += 1
            elif char_atual == '(':
                token = Token('ABRE_PARENTESE', char_atual)
                self.tokens.append(token)
                self.posicao += 1
            elif char_atual == ')':
                token = Token('FECHA_PARENTESE', char_atual)
                self.tokens.append(token)
                self.posicao += 1
            elif char_atual == '.':
                token = Token('PONTO', char_atual)
                self.tokens.append(token)
                self.posicao += 1
            elif char_atual == ',':
                token = Token('VIRGULA', char_atual)
                self.tokens.append(token)
                self.posicao += 1
            elif char_atual == '=':
                token = Token('IGUAL', char_atual)
                self.tokens.append(token)
                self.posicao += 1
            elif char_atual.isascii() and char_atual.isprintable():
                # Caracteres imprimíveis (exceto espaços) são tratados como literais
                token = self.obter_literal()
                self.tokens.append(token)
            else:
                # Lidar com outros casos conforme necessário
                self.posicao += 1

        return self.tokens

    def obter_identificador(self):
        inicio = self.posicao
        # Continua até encontrar um caractere que não seja alfanumérico ou sublinhado
        while self.posicao < len(self.codigo) and (self.codigo[self.posicao].isalnum() or self.codigo[self.posicao] == '_'):
            self.posicao += 1
        valor = self.codigo[inicio:self.posicao]
        return Token('IDENTIFICADOR', valor)

    def obter_numero(self):
        inicio = self.posicao
        # Continua até encontrar um caractere que não seja dígito
        while self.posicao < len(self.codigo) and self.codigo[self.posicao].isdigit():
            self.posicao += 1
        valor = self.codigo[inicio:self.posicao]
        return Token('NUMERO', valor)

    def obter_literal(self):
        inicio = self.posicao
        # Continua até encontrar um caractere que não seja imprimível ou espaço
        while self.posicao < len(self.codigo) and self.codigo[self.posicao].isascii() and self.codigo[self.posicao].isprintable() and not self.codigo[self.posicao].isspace():
            self.posicao += 1
        valor = self.codigo[inicio:self.posicao]
        return Token('LITERAL', valor)

    def ignorar_comentario(self):
        # Continua até encontrar um caractere de nova linha
        while self.posicao < len(self.codigo) and self.codigo[self.posicao] != '\n':
            self.posicao += 1

# Exemplo de uso:
codigo_fonte = """
# Programa cliente servidor de uma calculadora aritmética simples
c_channel calculadora computador_1 computador_2
SEQ
calculadora.send(operação, valor1, valor2, resultado)
calculadora.receive(operação, valor1, valor2, resultado)

# Execução paralela
PAR
# Cálculo do Fatorial (thread 1)
...
# Cálculo da Série de Fibonacci (thread 2)
...
"""
lexer = Lexer(codigo_fonte)
tokens = lexer.tokenize()
for token in tokens:
    print(f'Tipo: {token.tipo}, Valor: {token.valor}')


# Este código atualizado reconhece identificadores, números, literais e caracteres especiais de acordo com a nova gramática MiniPar.
# Certifique-se de ajustar e expandir as regras de tokenização conforme necessário para abranger todos os elementos da linguagem MiniPar.
