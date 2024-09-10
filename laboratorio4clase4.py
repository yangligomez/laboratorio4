#Actividad 1 
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
# Calcular el número de Fibonacci de 50
resultado = fibonacci(50)
print("Fibonacci de 50 es:", resultado)

#Actividad 2
from decimal import Decimal, getcontext
# Establecemos un contexto de precisión alta
getcontext().prec = 50
# Realizamos una operación matemática precisa
numero1 = Decimal('1.123456789123456789')
numero2 = Decimal('2.987654321987654321')
resultado = numero1 * numero2
# Mostramos el resultado con alta precisión
print(f"Resultado preciso: {resultado}")

#Actividad 3
import re
# Usamos una expresión regular avanzada para extraer palabras en mayúsculas de una cadena
cadena = "ESTO es un EJEMPLO de uso AVANZADO de CADENAS y Expresiones REGULARES."
# Expresión regular que busca palabras completamente en mayúsculas
patron = r'\b[A-Z]{2,}\b'
# Encontramos todas las coincidencias
palabras_mayusculas = re.findall(patron, cadena)
print("Palabras en mayúsculas:", palabras_mayusculas)

#Actividad 4
# Verificación de condiciones complejas usando operadores lógicos
a = True
b = False
c = True

# Uso de operadores lógicos avanzados (AND, OR, XOR)
resultado = (a and b) or (a and c) ^ b

print("Resultado de la operación lógica compleja:", resultado)

#Atividad 5
# Función que combina valores numéricos y maneja valores nulos
def sumar_o_default(a, b):
    # Si uno de los valores es None, retornamos 0 como valor predeterminado
    return (a or 0) + (b or 0)

# Ejemplo con diferentes combinaciones de enteros y valores None
print(sumar_o_default(5, None))  # Debería retornar 5
print(sumar_o_default(None, None))  # Debería retornar 0
print(sumar_o_default(10, 20))  # Debería retornar 30
