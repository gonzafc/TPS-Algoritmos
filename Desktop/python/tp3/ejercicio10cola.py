from clasecola import Cola
from clasestack import Stack

cola = Cola()
cola.arrive({"hora": "10:30", "app": "Facebook", "mensaje": "Nuevo comentario"})
cola.arrive({"hora": "11:00", "app": "Twitter", "mensaje": "Aprendiendo Java!"})
cola.arrive({"hora": "12:00", "app": "Facebook", "mensaje": "Nuevo like"})
cola.arrive({"hora": "13:00", "app": "Twitter", "mensaje": "Python es increíble"})
cola.arrive({"hora": "14:00", "app": "Instagram", "mensaje": "Nueva foto publicada"})
cola.arrive({"hora": "15:00", "app": "Facebook", "mensaje": "Nuevo mensaje privado"})

def eliminar_fb():
    cola_aux = Cola()
    while cola.size() > 0:
        mensaje = cola.attention()
        if mensaje["app"] != "Facebook":
            cola_aux.arrive(mensaje)
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())

def mostrar_twitter():
    cola_aux = Cola()
    while cola.size() > 0:
        mensaje = cola.attention()
        cola_aux.arrive(mensaje)
        if mensaje["app"] == "Twitter":
            print(f"{mensaje['hora']} - {mensaje['app']}: {mensaje['mensaje']}")
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())
        
def notis_entre_hora():
    pilanotis = Stack()
    colaaux = Cola()

    while cola.size() > 0:
        mensaje = cola.attention()
        colaaux.arrive(mensaje)
        if mensaje["hora"] >= "11:43" and mensaje["hora"] <= "15:57":
            pilanotis.push(mensaje)
    while colaaux.size() > 0:
        cola.arrive(colaaux.attention())
    return pilanotis

## sacar mensajes de facebook
cola.show()
print("")
eliminar_fb()
cola.show()

## mostrar mensajes de twitter
print("")
print("mensajes de twitter:")
print("")
mostrar_twitter()
print("")
## mostrar mensajes entre 11:43 y 15:57
print("")
print("mensajes entre 11:43 y 15:57:")
notis_entre_hora().show()
