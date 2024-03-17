SEQ
# Apresentar na tela as opções da calculadora (+, -, *, /)
print("Opções da calculadora: +, -, *, /")
# Ler a operação aritmética desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Ler o primeiro operando
valor1 = float(input("Digite o primeiro valor: "))

# Ler o segundo operando
valor2 = float(input("Digite o segundo valor: "))

# Enviar a operação e os valores para a calculadora
calculadora.send(operacao, valor1, valor2, resultado)

# Receber o resultado da calculadora
resultado = computador_1.receive()

# Imprimir o resultado
print("Resultado:", resultado)
