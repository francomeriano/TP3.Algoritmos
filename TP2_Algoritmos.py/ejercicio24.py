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

# Cargar pila de personajes
def cargar_pila():
    pila = []
    cantidad = int(input("¿Cuántos personajes vas a cargar? "))
    
    for i in range(cantidad):
        print(f"\nPersonaje #{i + 1}")
        nombre = input("Nombre: ")
        peliculas = int(input("Cantidad de películas en las que participó: "))
        personaje = {'nombre': nombre, 'peliculas': peliculas}
        apilar(pila, personaje)
    
    return pila

# Punto A
def buscar_rocket_groot(pila_original):
    pila_aux = []
    posicion = 1

    print("\n=== Punto A: Posición de Rocket Raccoon y Groot ===")
    while not pila_vacia(pila_original):
        personaje = desapilar(pila_original)
        if personaje['nombre'] in ['Rocket Raccoon', 'Groot']:
            print(f"✔ {personaje['nombre']} está en la posición {posicion} desde la cima.")
        apilar(pila_aux, personaje)
        posicion += 1

    while not pila_vacia(pila_aux):
        apilar(pila_original, desapilar(pila_aux))

# Punto B
def personajes_mas_de_5(pila_original):
    pila_aux = []

    print("\n=== Punto B: Personajes con más de 5 películas ===")
    while not pila_vacia(pila_original):
        personaje = desapilar(pila_original)
        if personaje['peliculas'] > 5:
            print(f"✔ {personaje['nombre']} participó en {personaje['peliculas']} películas.")
        apilar(pila_aux, personaje)

    while not pila_vacia(pila_aux):
        apilar(pila_original, desapilar(pila_aux))

# Punto C
def peliculas_black_widow(pila_original):
    pila_aux = []
    encontrado = False

    print("=== Películas de Black Widow ===")
    while not pila_vacia(pila_original):
        personaje = desapilar(pila_original)
        if personaje['nombre'] == 'Black Widow':
            print(f"✔ Black Widow participó en {personaje['peliculas']} películas.")
            encontrado = True
        apilar(pila_aux, personaje)

    while not pila_vacia(pila_aux):
        apilar(pila_original, desapilar(pila_aux))

    if not encontrado:
        print("✖ Black Widow no está en la pila.")

# Punto D
def personajes_c_d_g(pila_original):
    pila_aux = []
    letras_objetivo = ('C', 'D', 'G')

    print("=== Personajes que empiezan con C, D o G ===")
    while not pila_vacia(pila_original):
        personaje = desapilar(pila_original)
        if personaje['nombre'].startswith(letras_objetivo):
            print(f" {personaje['nombre']}")
        apilar(pila_aux, personaje)

    while not pila_vacia(pila_aux):
        apilar(pila_original, desapilar(pila_aux))

# prog principal
pila_personajes = cargar_pila()

buscar_rocket_groot(pila_personajes)   # Punto A

personajes_mas_de_5(pila_personajes)   # Punto B

peliculas_black_widow(pila_personajes) # Punto C

personajes_c_d_g(pila_personajes)      # Punto D
