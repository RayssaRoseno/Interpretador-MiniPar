# ParMini - Interpretador MiniPar

O ParMini é um interpretador desenvolvido em Python que permite a execução de programas escritos na linguagem MiniPar. Essa linguagem oferece suporte para a execução de instruções sequenciais e paralelas, incluindo comunicação entre computadores por meio de canais específicos.

## Características Principais:

- **Execução Sequencial e Paralela:** O ParMini possibilita a execução de blocos de código de forma sequencial e paralela, proporcionando flexibilidade na construção de programas concorrentes.

- **Comunicação entre Computadores:** A linguagem MiniPar inclui canais de comunicação que permitem a troca de mensagens entre diferentes computadores, implementado por meio de sockets em Python.

- **Suporte a Threads:** A execução paralela é implementada utilizando threads, permitindo que blocos de código sejam executados simultaneamente em um mesmo computador.

- **Tipos de Variáveis:** O interpretador suporta variáveis booleanas, inteiros e strings, oferecendo a flexibilidade necessária para o desenvolvimento de uma variedade de programas.

## Estrutura do Projeto:

- **Lexer (Analisador Léxico)**: Este módulo é responsável por dividir o código-fonte em unidades significativas chamadas tokens. Ele varre o código fonte e identifica palavras-chave, identificadores, operadores, símbolos especiais e outros elementos léxicos, atribuindo a cada um um tipo e um valor. Os tokens gerados pelo Lexer são utilizados pelo Parser para construir a estrutura de árvore sintática.

- **Parser (Analisador Sintático)**: O Parser recebe os tokens produzidos pelo Lexer e os utiliza para construir uma representação hierárquica do código fonte na forma de uma árvore sintática. Ele verifica se a estrutura do código fonte está de acordo com as regras da gramática da linguagem e produz uma estrutura de dados que representa a hierarquia e a relação entre os elementos do código fonte.

- **Interpreter (Interpretador)**: O Interpreter recebe a árvore sintática gerada pelo Parser e executa as instruções representadas por ela. Ele percorre a árvore e interpreta cada nó, realizando as operações correspondentes. Isso pode incluir a execução de instruções sequenciais, a criação e execução de threads para instruções paralelas, a manipulação de variáveis e a comunicação entre computadores por meio de canais.



## Como Usar:

1. **Instalação:**
```bash
   git clone https://github.com/RayssaRoseno/ParMini.git
   cd ParMini
```
2. Execução:
 ```bash
   python main.py
 ```

## Contribuições

[RayssaRoseno](https://github.com/RayssaRoseno)

