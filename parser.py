
class Node:
    def __init__(self, tipo, valor=None, filhos=None):
        self.tipo = tipo
        self.valor = valor
        self.filhos = filhos if filhos else []

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicao = 0
        self.current_token = self.tokens[self.posicao]

    def parse(self):
        return self.programa_minipar()

    def programa_minipar(self):
        bloco_stmt_node = self.bloco_stmt()
        return Node('programa_minipar', filhos=[bloco_stmt_node])

    def bloco_stmt(self):
        if self.current_token.tipo == 'SEQ':
            return self.bloco_SEQ()
        elif self.current_token.tipo == 'PAR':
            return self.bloco_PAR()
        else:
            # Se não encontrar um bloco, retorna um nó vazio
            return Node('vazio')

    def bloco_SEQ(self):
        self.match('SEQ')
        stmts_node = self.stmts()
        return Node('bloco_SEQ', filhos=[stmts_node])

    def bloco_PAR(self):
        self.match('PAR')
        stmts_node = self.stmts()
        return Node('bloco_PAR', filhos=[stmts_node])

    def stmts(self):
        stmt_node = self.stmt()
        if self.current_token.tipo == 'PONTO_VIRGULA':
            self.match('PONTO_VIRGULA')
            stmts_node = self.stmts()
            return Node('stmts', filhos=[stmt_node, stmts_node])
        else:
            return Node('stmts', filhos=[stmt_node])

    def stmt(self):
        if self.current_token.tipo == 'IDENTIFICADOR':
            return self.atribuicao()
        elif self.current_token.tipo == 'IF':
            return self.if_stmt()
        elif self.current_token.tipo == 'WHILE':
            return self.while_stmt()
        elif self.current_token.tipo == 'C_CHANNEL':
            return self.c_channel_stmt()
        elif self.current_token.tipo == 'SEND':
            return self.send_stmt()
        elif self.current_token.tipo == 'RECEIVE':
            return self.receive_stmt()
        else:
            raise Exception('Erro de sintaxe: stmt desconhecido')

    def atribuicao(self):
        id_node = self.id()
        self.match('IGUAL')
        expr_node = self.expr()
        self.match('PONTO_VIRGULA')
        return Node('atribuicao', filhos=[id_node, expr_node])

    def if_stmt(self):
        self.match('IF')
        self.match('ABRE_PARENTESE')
        bool_node = self.bool_expr()
        self.match('FECHA_PARENTESE')
        stmt1_node = self.stmt()
        if self.current_token.tipo == 'ELSE':
            self.match('ELSE')
            stmt2_node = self.stmt()
            return Node('if_stmt', filhos=[bool_node, stmt1_node, stmt2_node])
        else:
            return Node('if_stmt', filhos=[bool_node, stmt1_node])

    def while_stmt(self):
        self.match('WHILE')
        self.match('ABRE_PARENTESE')
        bool_node = self.bool_expr()
        self.match('FECHA_PARENTESE')
        stmt_node = self.stmt()
        return Node('while_stmt', filhos=[bool_node, stmt_node])

    def c_channel_stmt(self):
        self.match('C_CHANNEL')
        id1_node = self.id()
        id2_node = self.id()
        id3_node = self.id()
        self.match('PONTO_VIRGULA')
        return Node('c_channel_stmt', filhos=[id1_node, id2_node, id3_node])

    def send_stmt(self):
        id_node = self.id()
        self.match('PONTO')
        self.match('SEND')
        self.match('ABRE_PARENTESE')
        id1_node = self.id()
        self.match('VIRGULA')
        expr1_node = self.expr()
        self.match('VIRGULA')
        expr2_node = self.expr()
        self.match('VIRGULA')
        id2_node = self.id()
        self.match('FECHA_PARENTESE')
        self.match('PONTO_VIRGULA')
        return Node('send_stmt', filhos=[id_node, id1_node, expr1_node, expr2_node, id2_node])

    def receive_stmt(self):
        id_node = self.id()
        self.match('PONTO')
        self.match('RECEIVE')
        self.match('ABRE_PARENTESE')
        id1_node = self.id()
        self.match('VIRGULA')
        id2_node = self.id()
        self.match('VIRGULA')
        id3_node = self.id()
        self.match('VIRGULA')
        id4_node = self.id()
        self.match('FECHA_PARENTESE')
        self.match('PONTO_VIRGULA')
        return Node('receive_stmt', filhos=[id_node, id1_node, id2_node, id3_node, id4_node])

    def bool_expr(self):
        rel_expr_node = self.rel_expr()
        if self.current_token.tipo in ['&&', '||']:
            bool_op_node = Node('bool_op', valor=self.current_token.valor)
            self.match(self.current_token.tipo)
            bool_expr_tail_node = self.bool_expr()
            return Node('bool_expr', filhos=[rel_expr_node, bool_op_node, bool_expr_tail_node])
        else:
            return Node('bool_expr', filhos=[rel_expr_node])

    def rel_expr(self):
        expr1_node = self.expr()
        rel_op_node = Node('rel_op', valor=self.current_token.valor)
        self.match(self.current_token.tipo)
        expr2_node = self.expr()
        return Node('rel_expr', filhos=[expr1_node, rel_op_node, expr2_node])

    def expr(self):
        term_node = self.term()
        expr_tail_node = self.expr_tail()
        return Node('expr', filhos=[term_node, expr_tail_node])

    def expr_tail(self):
        if self.current_token.tipo in ['+', '-']:
            add_op_node = Node('add_op', valor=self.current_token.valor)
            self.match(self.current_token.tipo)
            term_node = self.term()
            expr_tail_node = self.expr_tail()
            return Node('expr_tail', filhos=[add_op_node, term_node, expr_tail_node])
        else:
            return Node('expr_tail')

    def term(self):
        factor_node = self.factor()
        term_tail_node = self.term_tail()
        return Node('term', filhos=[factor_node, term_tail_node])

    def term_tail(self):
        if self.current_token.tipo in ['*', '/']:
            mul_op_node = Node('mul_op', valor=self.current_token.valor)
            self.match(self.current_token.tipo)
            factor_node = self.factor()
            term_tail_node = self.term_tail()
            return Node('term_tail', filhos=[mul_op_node, factor_node, term_tail_node])
        else:
            return Node('term_tail')

    def factor(self):
        if self.current_token.tipo == 'ABRE_PARENTESE':
            self.match('ABRE_PARENTESE')
            expr_node = self.expr()
            self.match('FECHA_PARENTESE')
            return Node('factor', filhos=[expr_node])
        elif self.current_token.tipo == 'IDENTIFICADOR':
            return self.id()
        elif self.current_token.tipo == 'NUMERO':
            return self.numero()
        elif self.current_token.tipo == 'LITERAL':
            return self.literal()
        elif self.current_token.tipo == 'FIBONACCI':
            return self.fibonacci()
        elif self.current_token.tipo == 'FACTORIAL':
            return self.factorial()
        else:
            raise Exception('Erro de sintaxe: fator desconhecido')

    def id(self):
        token = self.current_token
        self.match('IDENTIFICADOR')
        return Node('id', valor=token.valor)

    def numero(self):
        token = self.current_token
        self.match('NUMERO')
        return Node('numero', valor=token.valor)

    def literal(self):
        token = self.current_token
        self.match('LITERAL')
        return Node('literal', valor=token.valor)

    def fibonacci(self):
        self.match('FIBONACCI')
        self.match('ABRE_PARENTESE')
        expr_node = self.expr()
        self.match('FECHA_PARENTESE')
        return Node('fibonacci', filhos=[expr_node])

    def factorial(self):
        self.match('FACTORIAL')
        self.match('ABRE_PARENTESE')
        expr_node = self.expr()
        self.match('FECHA_PARENTESE')
        return Node('factorial', filhos=[expr_node])

    def match(self, expected_token_type):
        if self.current_token.tipo == expected_token_type:
            self.advance()
        else:
            raise Exception(f'Erro de sintaxe: esperava-se {expected_token_type}, mas encontrou {self.current_token.tipo}')

    def advance(self):
        self.posicao += 1
        if self.posicao < len(self.tokens):
            self.current_token = self.tokens[self.posicao]


#Neste código, atualizei os métodos de acordo com a nova gramática, incluindo adições de novos métodos como send_stmt, receive_stmt, rel_expr, 
#fibonacci, factorial e outros, além de ajustar os métodos existentes para corresponder aos tokens e regras da gramática atual. 
#Certifique-se de que os tokens fornecidos ao parser correspondam à nova gramática.
            


