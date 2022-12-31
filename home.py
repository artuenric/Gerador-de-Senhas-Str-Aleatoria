import flet as ft
import random as rd
import string as st

def pg():
    """
    Creates a specific page to use with the "view", in this case, the main page or "home".
    """
    #For better readability, we put the functions and controls before the return with "view"

    container_hello = ft.Container(ft.Text("Olá! Você está na home."))
    go_to_help = ft.ElevatedButton(
                    "HELP",
                    on_click = lambda e: e.page.go("/help"))


    return ft.View(
        "/home", #Argument for route
        scroll = ft.ScrollMode.AUTO,
        controls= [
            container_hello,
            go_to_help
        ]
    )

#On ascii 8 bits: A = 65, Z = 90 and a = 97, z = 122
letter_lower = lambda: chr(rd.randint(97, 122))
letter_upper = lambda: chr(rd.randint(65, 90))
specials_chars = lambda: chr(rd.randint(33, 64))
number = lambda: rd.randint(0,9)

print(letter_lower(), letter_upper())

