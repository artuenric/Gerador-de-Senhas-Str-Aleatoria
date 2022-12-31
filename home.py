import flet as ft

def pg():
    """
    Creates a specific page to use with the "view", in this case, the main page or "home".
    """
    #For better readability, we put the functions and controls before the return with "view"
    
    container_hello = ft.Container(ft.Text("Olá! Você está na home."))
    go_to_help = ft.FilledButton(
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