import pyautogui
import time
import keyboard

segs = 0
pyautogui.click()


time.sleep(1)
# Función de click
def click(time_def):
    pyautogui.click()
    time.sleep(time_def)

def clicker_automatico():
    global segs
    click(0.5)
    click(0.5)
    segs += 1
    if keyboard.is_pressed('p'):
        print('Autoclicker pausado, presiona p para reanudar...')
        while True:
            time.sleep(1)
            if keyboard.is_pressed('p'):
                print('Reanudando')
                break
    if keyboard.is_pressed('o'):
        return False
    return True

def activar_click_izquierdo():
    print('Manteniendo click izquierdo')
    pyautogui.mouseDown(button='left')  # presionar click izquierdo

# Esta función debe mantener presionada la letra 'w' para que el personaje camine y mantener el click izquierdo
def minador():
    pyautogui.keyDown('W')
    activar_click_izquierdo()

print('------Autoclicker de Z0SO------')
print('Presiona 1 para activar el autoclicker')
print('Presiona 2 para activar el minador')

value = input('Ingrese el valor: ')

# Manejo de valores
if value == '1':
    print('Autoclicker activado !!')
    while True:
        if not clicker_automatico():
            break
elif value == '2':
    print('Minador activado !!')
    time.sleep(2)
    minador()
else:
    print('Valor incorrecto, intente de nuevo')

print('Autoclicker finalizado')
print(f'Hiciste {segs*2} clicks durante {segs} segundos !!')
