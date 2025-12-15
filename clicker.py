import time
import threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener as KeyboardListener

# Configuración
DELAY = 0.6 # Intervalo de click en segundos
mouse = MouseController()
clicking = False

def clicker():
    """Función que realiza el click en un bucle."""
    while True:
        if clicking:
            # Simula la pulsación y liberación del botón izquierdo
            mouse.click(Button.left)
            # Imprime para saber que el click se realizó (opcional)
            print(f"Click realizado. Esperando {DELAY} segundos.")
        
        # Espera el tiempo de retardo, esté clicando o no
        time.sleep(DELAY)

def on_press(key):
    """Función para manejar las pulsaciones de teclado."""
    global clicking
    try:
        # Usamos la tecla Bloq Mayús (Caps Lock) como interruptor (toggle)
        if key == Key.caps_lock:
            # Invierte el estado de 'clicking'
            clicking = not clicking
            print(f"--- Clicker {'INICIADO' if clicking else 'DETENIDO'} ---")
        
    except AttributeError:
        # Esto manejaría otras teclas que no tienen un '.char' (como Shift, Alt, etc.)
        pass

def on_release(key):
    """Función para detener el listener al presionar una tecla específica."""
    # Puedes usar 'esc' para salir completamente del programa
    if key == Key.esc:
        print("Saliendo del programa...")
        # Devuelve False para detener el listener
        return False

# Iniciar el hilo del clicker
# 'daemon=True' permite que el hilo se cierre cuando el programa principal termine
click_thread = threading.Thread(target=clicker, daemon=True)
click_thread.start()

# Iniciar el listener del teclado para iniciar/detener
print("Autoclicker iniciado.")
print("Presiona 'Bloq Mayús' (Caps Lock) para INICIAR/DETENER el clicker.")
print("Presiona 'Esc' para SALIR del programa.")

# Bloquea el programa principal, esperando los eventos del teclado
with KeyboardListener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Programa finalizado.")
