import random
from playsound import playsound
import os

# Función para reproducir sonido
def reproducir_sonido(nombre_archivo):
    # Obtener la ruta completa del archivo de sonido
    ruta = os.path.join(os.path.dirname(__file__), 'sonidos', nombre_archivo)
    try:
        playsound(ruta)
    except Exception as e:
        print(f"Error al reproducir {nombre_archivo}: {e}")

def bienvenida():
    reproducir_sonido('bienvenida.mp3')  # Sonido de bienvenida
    print("🏝️ ¡Bienvenido a la Aventura del Tesoro! 🏝️")
    print("Tienes que tomar decisiones inteligentes para encontrar el tesoro.")
    print("¿Estás listo para comenzar? ¡Vamos!\n")

def camino():
    reproducir_sonido('seleccion.mp3')  # Sonido de selección
    print("Te encuentras en una encrucijada.")
    print("1. Tomar el camino de la derecha 🌳")
    print("2. Tomar el camino de la izquierda 🏞️")
    eleccion = input("¿Qué camino eliges? (1 o 2): ")
    return eleccion

def enfrentar_enemigo():
    reproducir_sonido('enemigo.mp3')  # Sonido de encuentro con enemigo
    enemigos = ["dragón 🐉", "pirata 🏴‍☠️", "serpiente 🐍"]
    enemigo = random.choice(enemigos)
    print(f"¡Oh no! Te has encontrado con un {enemigo} en tu camino.")
    print("1. Luchar 🗡️")
    print("2. Huir 🏃‍♂️")
    accion = input("¿Qué decides hacer? (1 o 2): ")
    
    if accion == "1":
        reproducir_sonido('pelea.mp3')  # Sonido de pelea
        if random.randint(1, 2) == 1:
            reproducir_sonido('victoria.mp3')  # Sonido de victoria
            print(f"¡Ganaste la batalla contra el {enemigo}! 🎉\n")
            return True
        else:
            reproducir_sonido('derrota.mp3')  # Sonido de derrota
            print(f"Has sido derrotado por el {enemigo}... 😢\n")
            return False
    else:
        reproducir_sonido('huir.mp3')  # Sonido de huida
        print("¡Escapaste con éxito! Pero has perdido tiempo... ⏳\n")
        return True

def buscar_tesoro():
    reproducir_sonido('busqueda.mp3')  # Sonido de búsqueda
    print("Has llegado a una cueva misteriosa.")
    print("1. Entrar en la cueva 🕯️")
    print("2. Seguir explorando afuera 🚶‍♂️")
    eleccion = input("¿Qué decides hacer? (1 o 2): ")
    
    if eleccion == "1":
        reproducir_sonido('tesoro.mp3')  # Sonido de tesoro encontrado
        if random.randint(1, 3) == 3:
            reproducir_sonido('victoria.mp3')  # Sonido de victoria
            print("🎉 ¡Has encontrado el tesoro mágico! ¡Felicidades! 🏆💰\n")
            return True
        else:
            reproducir_sonido('fallo.mp3')  # Sonido de fallo
            print("La cueva está vacía... Sigue buscando. 🔍\n")
            return False
    else:
        reproducir_sonido('seleccion.mp3')  # Sonido de selección
        print("Decidiste no entrar. Sigues explorando...\n")
        return False

def aventura():
    bienvenida()
    
    # Primera decisión de caminos
    eleccion_camino = camino()
    
    if eleccion_camino == "1":
        reproducir_sonido('camino_derecha.mp3')  # Sonido camino derecho
        print("Tomaste el camino de la derecha y avanzas por el bosque.")
    elif eleccion_camino == "2":
        reproducir_sonido('camino_izquierda.mp3')  # Sonido camino izquierdo
        print("Tomaste el camino de la izquierda y sigues por una playa solitaria.")
    else:
        reproducir_sonido('error.mp3')  # Sonido de error
        print("Elección no válida. Estás perdido en la isla. 🏝️\n")
        return
    
    # Enfrentando un enemigo
    si_superaste_enemigo = enfrentar_enemigo()
    if not si_superaste_enemigo:
        reproducir_sonido('fin.mp3')  # Sonido de fin
        print("Fin de la aventura. ¡Inténtalo de nuevo!\n")
        return
    
    # Buscar el tesoro
    si_encontraste_tesoro = buscar_tesoro()
    if si_encontraste_tesoro:
        reproducir_sonido('victoria.mp3')  # Sonido de victoria final
        print("¡Eres el gran aventurero de la isla del tesoro! 🎉\n")
    else:
        reproducir_sonido('fallo_final.mp3')  # Sonido de fallo final
        print("El tesoro sigue perdido. ¡Sigue buscando en otra aventura!\n")

# Iniciar la aventura
aventura()
