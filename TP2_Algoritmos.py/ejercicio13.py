# Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni
# verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se 
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver 
# las siguientes actividades:
#  a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, 
#     además mostrar el nombre de dichas películas;
#  b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
#  c. eliminar los modelos de los trajes destruidos mostrando su nombre;
#  d. un modelo de traje puede usarse en más de una película y en una película se pueden usar 
#     más de un modelo de traje, estos deben cargarse por separado;
#  e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos 
#     repetidos en una misma película;
#  f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y 
#     “Capitan America: Civil War”.

# === Funciones de pila ===
def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    return pila.pop()

def pila_vacia(pila):
    return len(pila) == 0

def cima(pila):
    return pila[-1]

def tamaño(pila):
    return len(pila)

# CARGO DATOS
# Función para cargar datos de trajes
def cargar_trajes(pila):
    while True:
        modelo = input("Modelo del traje: ")
        pelicula = input("Película donde se usó: ")
        estado = input("Estado final (dañado / impecable / destruido): ")
        
        apilar(pila, {
            'modelo': modelo,
            'pelicula': pelicula,
            'estado': estado
        })
        
        continuar = input("¿Desea cargar otro traje? (s/n): ").lower()
        if continuar != 's':
            break

# PUNTO A
def buscar_hulkbuster(pila):
    aux = []
    encontrado = False
    while not pila_vacia(pila):
        traje = desapilar(pila)
        aux.append(traje)
        if traje['modelo'] == 'Mark XLIV':
            print(f"Se usó en: {traje['pelicula']}")
            encontrado = True
    while aux:
        apilar(pila, aux.pop())
    if not encontrado:
        print("El modelo Mark XLIV no se utilizó en ninguna película.")

# PUNTO B
def mostrar_dañados(pila):
    aux = []
    while not pila_vacia(pila):
        traje = desapilar(pila)
        if traje['estado'] == 'dañado':
            print(f"Modelo: {traje['modelo']} (Película: {traje['pelicula']})")
        aux.append(traje)
    while aux:
        apilar(pila, aux.pop())

# PUNTO C
def eliminar_destruidos(pila):
    aux = []
    while not pila_vacia(pila):
        traje = desapilar(pila)
        if traje['estado'] == 'destruido':
            print(f"Eliminado: {traje['modelo']} (Película: {traje['pelicula']})")
        else:
            aux.append(traje)
    while aux:
        apilar(pila, aux.pop())

# PUNTO E
def agregar_mark_lxxxv(pila, pelicula):
    aux = []
    repetido = False
    while not pila_vacia(pila):
        traje = desapilar(pila)
        if traje['modelo'] == 'Mark LXXXV' and traje['pelicula'] == pelicula:
            repetido = True
        aux.append(traje)
    if not repetido:
        apilar(aux, {'modelo': 'Mark LXXXV', 'pelicula': pelicula, 'estado': 'Impecable'})
        print(f"Se agregó Mark LXXXV en {pelicula}")
    else:
        print(f"Ya existe Mark LXXXV en {pelicula}, no se agregó.")
    while aux:
        apilar(pila, aux.pop())

# PUNTO F
def mostrar_trajes_peliculas(pila):
    aux = []
    peliculas_objetivo = ["Spider-Man: Homecoming", "Capitan America: Civil War"]
    while not pila_vacia(pila):
        traje = desapilar(pila)
        if traje['pelicula'] in peliculas_objetivo:
            print(f"Modelo: {traje['modelo']} (Película: {traje['pelicula']})")
        aux.append(traje)
    while aux:
        apilar(pila, aux.pop())

# programa principal
pila_trajes = []
cargar_trajes(pila_trajes)
print()
print("--- Buscar Hulkbuster ---")
buscar_hulkbuster(pila_trajes)
print()
print("--- Modelos dañados ---")
mostrar_dañados(pila_trajes)
print()
print("--- Eliminar destruidos ---")
eliminar_destruidos(pila_trajes)
print()
print("--- Cargar Mark LXXXV (sin duplicar) ---")
pelicula = input("¿En qué película querés agregar Mark LXXXV?: ")
agregar_mark_lxxxv(pila_trajes, pelicula)
print()
print("--- Trajes usados en spider man Homecoming y Civil War ---")
mostrar_trajes_peliculas(pila_trajes)
print()