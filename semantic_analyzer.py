class SemanticAnalyzer:
    def __init__(self):
        self.errors = []

    def analyze(self, node):
        self.errors = []
        self.visit(node)
        if self.errors:
            for error in self.errors:
                print(f"Erro Semântico: {error}")
        else:
            print("Análise Semântica Concluída sem Erros.")

    def visit(self, node):
        # Obtém o nome do método de visita específico para o tipo de nó atual
        method_name = 'visit_' + type(node).__name__
        # Verifica se o método de visita específico existe para o tipo de nó atual
        visitor = getattr(self, method_name, self.generic_visit)
        # Chama o método de visita específico ou o método de visita genérico se não existir um específico
        visitor(node)

    def generic_visit(self, node):
        # Visita todos os filhos do nó atual
        for child in node.filhos:
            self.visit(child)

    # Métodos de visita específicos para diferentes tipos de nós

    def visit_programa_minipar(self, node):
        self.generic_visit(node)

    def visit_bloco_stmt(self, node):
        self.generic_visit(node)

    def visit_bloco_SEQ(self, node):
        self.generic_visit(node)

    def visit_bloco_PAR(self, node):
        self.generic_visit(node)

    def visit_stmts(self, node):
        self.generic_visit(node)

    def visit_atribuicao(self, node):
        self.generic_visit(node)

    def visit_if_stmt(self, node):
        self.generic_visit(node)

    def visit_while_stmt(self, node):
        self.generic_visit(node)

    def visit_c_channel_stmt(self, node):
        self.generic_visit(node)

    def visit_send_stmt(self, node):
        self.generic_visit(node)

    def visit_receive_stmt(self, node):
        self.generic_visit(node)

    def visit_bool_expr(self, node):
        self.generic_visit(node)

    def visit_rel_expr(self, node):
        self.generic_visit(node)

    def visit_expr(self, node):
        self.generic_visit(node)

    def visit_term(self, node):
        self.generic_visit(node)

    def visit_factor(self, node):
        self.generic_visit(node)

    def visit_id(self, node):
        self.generic_visit(node)

    def visit_numero(self, node):
        self.generic_visit(node)

    def visit_literal(self, node):
        self.generic_visit(node)

    def visit_fibonacci(self, node):
        self.generic_visit(node)

    def visit_factorial(self, node):
        self.generic_visit(node)

    def visit_c_channel_access(self, node):
        self.generic_visit(node)

    # Exemplo de verificação semântica para a execução sequencial dentro de um bloco PAR
    def visit_execucao_paralela(self, node):
        # Itera pelos filhos do nó para encontrar execuções sequenciais dentro de blocos PAR
        for child in node.filhos:
            if child.tipo == 'execucao' and 'SEQ' in [stmt.tipo for stmt in child.filhos]:
                self.errors.append("Erro Semântico: Execução sequencial dentro de um bloco PAR.")
                break
