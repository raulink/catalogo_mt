import flet as ft

# Importar todo de logins
from ui.ButtonRed import ButtonRed
from ui.Etiquetas import Etiquetas


conteiner = ft.Container(
    border_radius=20,
    width=320,
    height=500,
    gradient=ft.LinearGradient([
        ft.colors.PURPLE,
        ft.colors.PINK,
        ft.colors.RED,
    ])
)

def main(page:ft.Page):

    # COndiguracion de la pagina
    page.bgcolor= ft.colors.BLACK
    page.vertical_alignment= "center"
    page.horizontal_alignment = "center"

    page.add(
        conteiner,   
        ButtonRed(),
        Etiquetas("Hola",ft.icons.EMAIL ),
        Etiquetas("Mundo",ft.icons.PASSWORD),
        
    )

ft.app(target=main)