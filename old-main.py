import pyautogui
import time
import time

tiempo=0

def minador():
    global tiempo
    
    print("Iniciando minado en 3 segundos...")
    time.sleep(1)
    print("Iniciando minado en 2 segundos...")
    time.sleep(1)
    print("Iniciando minado en 1 segundos...")
    time.sleep(1)

    print("Presionando 'W' y manteniendo el click izquierdo...")
    pyautogui.keyDown('w')  # Mantén la tecla 'W' presionada
    pyautogui.mouseDown(button='left')  # Mantén presionado el click izquierdo

    # con este while se puede ver el tiempo que lleva minando y ademas forzamos a la interrupcion del programa
    while True:
        time.sleep(1)
        tiempo += 1
        print(f"Minando durante {tiempo} segundos")


if __name__ == "__main__":
    try:
        minador()
    except KeyboardInterrupt:
        pyautogui.keyUp('w')  # Suelta la tecla 'W'
        pyautogui.mouseUp(button='left')
        print("Saliendo del programa...")
        print(f"Minaste duramente durante {tiempo} segundos ;)")

