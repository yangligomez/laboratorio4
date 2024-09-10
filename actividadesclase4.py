#actividad 1
numeros = [1,2,3,4,5,6,7,8,9,10]
cuadrados = [numero ** 2 for numero in numeros]
print("lista de numeros elevados al cuadrado:", cuadrados)
#actividad 2
nombre = "yang li "
edad = 23
mensaje = f"hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)
#actividad 3
edad = 23 
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
#Actividad 4
saldo = 1500.000
while saldo > 100.000:
    retiro = 115.000
    saldo -= retiro
    print(f"se ha retirado {retiro}, saldo actual:{saldo}.")
#Actividad 5
persona = {
    "nombre":"Yang li",
    "edad": 23, 
    "ciudad": "Sevilla"
}
for clave, valor in persona.items():
    print(f"{clave.capitalize()}:{valor}")
    

