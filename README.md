# ParMini - Interpretador MiniPar

O ParMini é um interpretador desenvolvido em Python que permite a execução de programas escritos na linguagem MiniPar. Essa linguagem oferece suporte para a execução de instruções sequenciais e paralelas, incluindo comunicação entre computadores por meio de canais específicos.

## Características Principais:

- **Execução Sequencial e Paralela:** O ParMini possibilita a execução de blocos de código de forma sequencial e paralela, proporcionando flexibilidade na construção de programas concorrentes.

- **Comunicação entre Computadores:** A linguagem MiniPar inclui canais de comunicação que permitem a troca de mensagens entre diferentes computadores, implementado por meio de sockets em Python.

- **Suporte a Threads:** A execução paralela é implementada utilizando threads, permitindo que blocos de código sejam executados simultaneamente em um mesmo computador.

- **Tipos de Variáveis:** O interpretador suporta variáveis booleanas, inteiros e strings, oferecendo a flexibilidade necessária para o desenvolvimento de uma variedade de programas.

## Estrutura do Projeto:

- **Lexer e Parser:** Módulos responsáveis pela análise léxica e sintática do código fonte, convertendo-o em uma árvore sintática.

- **Interpreter:** Módulo que executa as instruções representadas pela árvore sintática, gerenciando a execução sequencial e paralela.

- **Error Handler:** Módulo dedicado ao tratamento de erros, garantindo uma experiência de usuário aprimorada.

## Como Usar:

1. **Instalação:**
   ```bash
   git clone https://github.com/RayssaRoseno/ParMini.git
   cd ParMini
2. Execução:
 ```bash
   python main.py
 ```
3.  Programas de Teste:
```bash
Explore os programas de teste no diretório test/ para entender melhor a sintaxe e funcionalidades do MiniPar.
 ```
## Contribuições

@rayssaroseno
