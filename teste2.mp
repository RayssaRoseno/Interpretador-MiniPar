# Execução paralela
PAR
# Cálculo do Fatorial (thread 1)
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

resultado_fatorial = fatorial(5)
print("Fatorial de 5:", resultado_fatorial)

# Cálculo da Série de Fibonacci (thread 2)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

resultado_fibonacci = fibonacci(10)
print("Termo 10 da Série de Fibonacci:", resultado_fibonacci)
