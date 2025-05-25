"""
Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce 
el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
–por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, 
Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
 a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
 b. mostrar los nombre de los superhéroes femeninos;
 c. mostrar los nombres de los personajes masculinos;
 d. determinar el nombre del superhéroe del personaje Scott Lang;
 e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
 f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre  de superhéroes
"""

def arribo(cola, elemento):
    cola.append(elemento)

def atencion(cola):
    return cola.pop(0) if not cola_vacia(cola) else None

def cola_vacia(cola):
    return len(cola) == 0

def en_frente(cola):
    return cola[0] if not cola_vacia(cola) else None

def tamaño(cola):
    return len(cola)

def mover_al_final(cola):
    if not cola_vacia(cola):
        arribo(cola, atencion(cola))
        
        
# a
def personaje_de_capitana_marvel(cola):
    for _ in range(tamaño(cola)):
        dato = atencion(cola)
        if dato["superheroe"] == "Capitana Marvel":
            print("Personaje:", dato["personaje"])
        arribo(cola, dato)

# b
def superheroes_femeninos(cola):
    for _ in range(tamaño(cola)):
        dato = atencion(cola)
        if dato["genero"] == "F":
            print("Superhéroe femenino:", dato["superheroe"])
        arribo(cola, dato)

# c
def personajes_masculinos(cola):
    for _ in range(tamaño(cola)):
        dato = atencion(cola)
        if dato["genero"] == "M":
            print("Personaje masculino:", dato["personaje"])
        arribo(cola, dato)

# d
def superheroe_de_scott_lang(cola):
    for _ in range(tamaño(cola)):
        dato = atencion(cola)
        if dato["personaje"] == "Scott Lang":
            print("Superhéroe:", dato["superheroe"])
        arribo(cola, dato)

# e
def nombres_con_s(cola):
    for _ in range(tamaño(cola)):
        dato = atencion(cola)
        if dato["personaje"].startswith("S") or dato["superheroe"].startswith("S"):
            print("Dato con S:", dato)
        arribo(cola, dato)

# f
def buscar_carol_danvers(cola):
    encontrado = False
    for _ in range(tamaño(cola)):
        dato = atencion(cola)
        if dato["personaje"] == "Carol Danvers":
            print("Carol Danvers es:", dato["superheroe"])
            encontrado = True
        arribo(cola, dato)
    if not encontrado:
        print("Carol Danvers no se encuentra en la cola.")
        
