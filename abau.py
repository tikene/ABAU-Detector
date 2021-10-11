from colorama import init, Fore, Style
from time import sleep
from datetime import datetime
from playsound import playsound
import requests
import json
import os

init(convert=True)
init(autoreset=True)

bright = Style.BRIGHT
dim = Style.DIM
red = Fore.RED + bright + dim
green = Fore.GREEN + bright + dim
cyan = Fore.CYAN + bright + dim
yellow = Fore.LIGHTYELLOW_EX + bright + dim
blue = Fore.BLUE + bright + dim
magenta = Fore.MAGENTA + bright + dim


LOCATION_URL = "https://www.edu.xunta.es/CONTINXENCIA_NERTA/index.html"
SOUND_FILE = "bruh.wav"
DETECTION_STR = "deshabilitado temporalmente"
DELAY = 10


def main():
    os.system("cls")
    os.system("title Bot notas ABAU")

    print(magenta + "\n\n* Bot notas ABAU *\n")

    while True:
        try:
            abau = requests.get(LOCATION_URL)
        except Exception as e:
            print(red + "ERROR")
            print(e)
            sleep(DELAY)
            continue


        if abau.status_code != 200:
            os.system("msg * CODIGO ERROR")
            continue


        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        if DETECTION_STR in abau.text:
            print(yellow + "Las notas aún no han sido publicadas" + Fore.RESET + " - " + cyan + current_time)
        else:
            print(green + "NOTAS PUBLICADAS!!")
            playsound(SOUND_FILE)
            os.system("msg * Notas ABAU publicadas!")
            break


        sleep(DELAY)

main()
