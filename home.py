#Interface
import flet as ft
#Generate random string
import random as rd
#Regex
import re


#For better readability, we put the functions and controls before the return with "view"
def pg():
    """
    Creates a specific page to use with the "view", in this case, the main page or "home".
    """

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
        psswd = ""

        for genrt in range(size):
            decide = choose_new_char()
            if decide == 1:
                psswd += lowercase()
            elif decide == 2:
                psswd += number()
            elif decide == 3:
                psswd += uppercase()
            elif decide == 4:
                psswd += specials_chars()

        size_on_text.update()
        text_box.value = psswd 
        text_box.update()


    size_on_text = ft.Text()
    slider = ft.Slider(
                        width = 500,
                        min = 4,
                        max = 50,
                        opacity = 40,
                        active_color= "#B6D094",
                        thumb_color = "#B6D094",
                        value = 4,
                        on_change = change_slider
                        )
    
    #Level of security
    def number_and_letters(string):
        if re.search(r'[a-zA-Z]', string) and re.search(r'\d', string):
            return True
        return False

    def and_special_char(string):
        if number_and_letters(string):
            if re.search(r'[\w\s]'):
                return True
        return False

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

    #Copypaste
    
    #Interface structure
    base = ft.ResponsiveRow(
            [
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                    ft.Container(
                        content = ft.Text("Deslize para mudar o tamanho da senha"))
                    ]),
                ft.Column(
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    width = 500,
                    col = 12,
                    controls = [
                    ft.Container(
                        alignment = ft.alignment.top_center,
                        content = text_box),
                    ft.Container(
                        content = msg),
                    ft.Container(
                        content = slider),
                    ft.Row(
                        col = 2,
                        alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                        controls = [
                            ft.Container(
                                width = 30,
                                content = again_button), 
                            ft.Container(
                                width = 120,
                                content = size_on_text)
                            ])
                    ]
                )   
            ]
        )

    #What return for view
    return ft.View(
        "/home", #Argument for route
        bgcolor = "#00070D",
        scroll = ft.ScrollMode.AUTO,
        controls= [
            base
        ]
    )