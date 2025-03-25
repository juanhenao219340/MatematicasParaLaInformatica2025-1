def fibonacci(n):
    # Casos base
    if n <= 1:
        return n
    # Llamada recursiva
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo de uso
n = int(input("Introduce un número para calcular su Fibonacci: "))
print(f"El número Fibonacci en la posición {n} es: {fibonacci(n)}")