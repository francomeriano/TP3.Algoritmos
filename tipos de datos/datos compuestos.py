# LISTAS Y TUPLAS
# la lista empieza de posicion 0
lista = ["lucas", "soy dalto", True, 1.80] # la lista se puede modificar
tupla = ("lucas", "soy dalto", True, 1.80) # la tupla no se puede modificar
lista[1] = "soy franco" # ejemplo de como modifico list
print(lista[1])

# creando un conjunto (SET). No se modifican, no se puede acceder a elementos por indice
conjunto = {"lucas", "soy dalto", True, 1.80}
print(conjunto)

# creadno un diccionario (DICT)
diccionario = {
    "nombre" : "lucas dalto",
    "canal" : "soy dalto",
    "esta_contento" : True,
    "altura" : 1.80  
}
print(diccionario["nombre"])