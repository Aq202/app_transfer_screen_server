import pyautogui as gui
import os
from datetime import date, datetime
from pynput.keyboard import Listener
from pygame import mixer
from PIL import ImageGrab
import requests

count = 0
transfer = False
imageCreated = None

print("Presiona la tecla '|' tres veces para tomar una captura.")


def getDirectoryName():
    # ruta capturas/fecha/n.png
    current_date = date.today()
    return f"{current_date}"


def getFileName(extension="jpg"):
    # ruta capturas/fecha/n.png
    current_date = date.today()
    currentTime = datetime.now().time().strftime("%H-%M-%S")
    path = f"./{current_date}"

    # creando carpeta si no existe
    if not os.path.isdir(path):
        os.mkdir(path)

    # obteniendo numero de captura actual
    currentScreenIndex = len(os.listdir(path)) + 1

    return f"{currentTime} {currentScreenIndex}.{extension}"


def takeScreen():
    try:

        path = getDirectoryName()
        fileName = getFileName()
        filePath = f"./{path}/{fileName}"

        # Capturar pantalla.
        screenshot = gui.screenshot()
        screenshot.save(filePath)

        return fileName

    except Exception as ex:
        print(ex)
        return None


def playSound():
    try:
        mixer.init()  # initiate the mixer instance
        # loads the music, can be also mp3 file.
        mixer.music.load('notification.mp3')
        mixer.music.play()  # plays the music
    except:
        pass


def saveImageFromClipboard():

    path = getDirectoryName()
    fileName = getFileName("png")
    filePath = f"./{path}/{fileName}"

    img = ImageGrab.grabclipboard()  # obtener img de portapapeles
    # guardar imagen
    img.save(filePath, 'PNG')

    return fileName


def sendImageToServer(imageName):
    current_dir = os.getcwd()
    file_path = f"{current_dir}\\{getDirectoryName()}\\{imageName}"
    data = {'imagePath': file_path}
    response = requests.post("http://localhost:2004/transfer", json=data)
    print(response)
# key evenet callback


def key_pressed(key):

    global count, transfer, imageCreated

    key = str(key).replace("'", "")
    

    print(key)

    if(key == "|"):
        count += 1
        if(count == 3):
            imageCreated = takeScreen()
            playSound()

            count = 0  # resetear variable

    elif(key == "t" and count == 2):
        transfer = True
        count = 0

    elif(key == "s" and count == 2):  # combinación ||s guarda imagen de portapapeles
        # guardar imagen
        try:
            imageCreated = saveImageFromClipboard()
            playSound()
        except Exception:
            print("¡Cuidado! El contenido del portapapeles no es una imagen.")

        count = 0  # resetear el contador
    else:
        count = 0
        transfer = False

    if imageCreated != None and transfer == True:
        sendImageToServer(imageCreated)
        transfer = False
    elif imageCreated != None:
        transfer = False


# key event listener
with Listener(on_press=key_pressed) as l:
    l.join()
