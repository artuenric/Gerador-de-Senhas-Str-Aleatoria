import flet as ft
from flet import Page
#AAAAAAAAA
#To use the view and control your routes
from home import pg as v1
from help import pg as v2


def main(page: Page):
    """
    Basic function of flet creation
    """
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

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

    #remove top view
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    #call the rout functions
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
    #Views (as the command is done with the append, the last to be inserted is the first page to be directed)
    page.views.append(help)
    page.views.append(home)
    page.update()

ft.app(target=main)

