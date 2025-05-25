# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, 
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, 
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya 
#   la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 
#   11:43 y las 15:57, y determinar cuántas son.
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
def eliminar_facebook(cola):
    for _ in range(tamaño(cola)):
        notificacion = atencion(cola)
        if notificacion["aplicacion"] != "Facebook":
            arribo(cola, notificacion)

# b
def mostrar_twitter_python(cola):
    for _ in range(tamaño(cola)):
        notificacion = atencion(cola)
        if (notificacion["aplicacion"] == "Twitter" and "Python" in notificacion["mensaje"]):
            print(notificacion)
        arribo(cola, notificacion)
        
# c
def notificaciones_en_rango(cola):
    pila = []
    contador = 0

    for _ in range(tamaño(cola)):
        notificacion = atencion(cola)
        hora = notificacion["hora"]

        if "11:43" <= hora <= "15:57":
            pila.append(notificacion)
            contador += 1

        arribo(cola, notificacion)

    return contador, pila


