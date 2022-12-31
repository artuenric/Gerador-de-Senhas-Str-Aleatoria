import flet as ft
from flet import Page

#To use the view and control your routes
from home import pg as v1
from help import pg as v2

def main(page: Page):
    """
    Basic function of flet creation
    """

    #Title window
    page.title = "Gerador de Senhas"
    home = v1()
    help = v2()

    def route_change(route):
        """
        Allows navigation and choice of the page through the "view"
        """
        page.views.clear()
        if page.route == "/home":
            page.views.append(home)
        if page.route == "/help":
            page.views.append(help)
        page.update()

    #call the rout functions
    page.on_route_change = route_change
    page.go(page.route)

    #Views (as the command is done with the append, the last to be inserted is the first page to be directed)
    page.views.append(home)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)

#Notas: preciso adicionar aquela função view_pop pra testar a navegação e o histórico das páginas.