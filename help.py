import flet as ft

def pg():
    """
    Creates a specific page to use with the "view", in this case, the page for more informations.
    """
    #For better readability, we put the functions and controls before the return with "view"

    container_hello = ft.Container(ft.Text("Olá! Você está na página de ajuda."))
    go_to_home = ft.FilledButton("HOME",
                    on_click = lambda e: e.page.go("/home"))

    return ft.View(
        "/help", #Argument for route
        scroll = ft.ScrollMode.AUTO,
        controls= [
            container_hello,
            go_to_home    
        ]
    )