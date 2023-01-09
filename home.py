#Interface
import flet as ft
#Generate random string
import random as rd
#Regex
import re
#Any functions
from myfunctions import *

#For better readability, we put the functions and controls before the return with "view"
def pg():
    """
    Creates a specific page to use with the "view", in this case, the main page or "home".
    """

    #Characters types
    #Based on table ascii 8 bits
    lowercase = lambda: chr(rd.randint(97, 122))
    number = lambda: chr(rd.randint(48,57))
    #These types will be optional
    uppercase = lambda: chr(rd.randint(65, 90))
    specials_chars = lambda: chr(rd.randint(33, 47))

    #Enable more types to characters
    enable_upper = True
    enable_special = True

    #Decision of the types of characters
    choose_new_char = lambda: rd.randint(1,4)

   
    #Change string size
    def change_slider(e):

        if slider.value <= 10:    nice = ':('
        elif slider.value <= 15:  nice = ':|'
        elif slider.value <= 25:  nice = ':)'
        elif slider.value <= 40:  nice = ':D'
        else:                     nice = ':O'
        
        size_on_text.value = f"{slider.value:.0f} caracteres! {nice}"
        size = int(slider.value//1)
        passwd = ""

        for genrt in range(size):
            decide = choose_new_char()
            if decide == 1:
                passwd += lowercase()
            elif decide == 2:
                passwd += number()
            elif decide == 3:
                passwd += uppercase()
            elif decide == 4:
                passwd += specials_chars()

        size_on_text.update()
        text_box.value = passwd 
        text_box.update()


    size_on_text = ft.Text(
        text_align = ft.TextAlign.CENTER)
    slider = ft.Slider(
                        min = 4,
                        max = 50,
                        opacity = 40,
                        active_color= "#B6D094",
                        thumb_color = "#B6D094",
                        value = 4,
                        on_change = change_slider)
    

    #Is coming:
        #Copypaste
        #How safe?
    """
    def how_safe(e):
        quant_slider_size = int(slider.value//1)
        quant_text_box = len(text_box.value)

        if text_box.value.isdigit():
 
        elif text_box.value.islower():

        elif text_box.value.isalpha():
  
        elif number_and_letters(text_box.value):

        elif and_special_char(text_box.value): 
    """

    text_box = ft.TextField(
            cursor_color = "#B6D094",
            border_width = 2,
            border_color = "#B6D094",
            focused_border_color = "#F0F5FA",
            width = 450,
            height = 80,
            label = "Sua senha:",
            label_style = ft.TextStyle(color="#F0F5FA")
            #on_change = how_safe
    )
 
    msg = ft.Text()
    again_button = ft.IconButton(
            ft.icons.REPLAY_CIRCLE_FILLED,
            width = 40,
            height = 40,
            icon_size = 30,
            icon_color = "#B6D094",
            on_click = change_slider)


    #Interface structure
    base = ft.Column(
        height = 700,
        col = 12,
        alignment = ft.MainAxisAlignment.CENTER,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        spacing = 0,
        controls = [
            ft.ResponsiveRow(
                width = 450,
                controls = [ft.Text(
                    text_align = "center",
                    value = "Deslize para mudar o tamanho da senha\n")]),
            ft.ResponsiveRow(
                width = 400,
                controls = [text_box]),
            ft.ResponsiveRow(
                width = 450,
                controls = [slider]),
            ft.ResponsiveRow(
                width = 400,
                controls = [
                    ft.Row(
                        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls = [
                            size_on_text, 
                            again_button])
                        ]),
            ft.ResponsiveRow(
                width = 350,
                controls = [msg]),
            ]
        )

    #What return for view
    return ft.View(
        "/home", #Argument for route
        bgcolor = "#00070D",
        scroll = ft.ScrollMode.AUTO,
        vertical_alignment = ft.MainAxisAlignment.CENTER,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls= [
            base
        ]
    )