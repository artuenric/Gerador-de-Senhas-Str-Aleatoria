import flet as ft
import random as rd
import string as st
import re

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

#Characteres types
#Based on table ascii 8 bits
lowercase = lambda: chr(rd.randint(97, 122))
number = lambda: chr(rd.randint(48,57))
#These types will be optional
uppercase = lambda: chr(rd.randint(65, 90))
specials_chars = lambda: chr(rd.randint(33, 47))

#Habilit more types to characters
habilit_upper = True
habilit_special = True

#Random string features
size = 20
psswd = ""

#Decision of the types of characters
choose_new_char = lambda: rd.randint(1,4)

#Finally generate string
for generate in range(size):
    decide = choose_new_char()
    if decide == 1:
        psswd += lowercase()

    elif decide == 2:
        psswd += number()

    elif decide == 3:
        psswd += uppercase()

    elif decide == 4:
        psswd += specials_chars()

print(psswd)
