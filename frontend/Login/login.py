# Magno Efren 
# https://www.youtube.com/@MagnoEfren/videos

import flet as ft

# from ui.Contenedor import Contenedor
from  ui.Contenedor import *

def main(page:ft.Page):
    page.window_width =800
    page.window_height = 520
    page.padding = 0
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    #page.window_bgcolor = ft.colors.TRANSPARENT
    #page.window_title_bar_buttons_hidden = True
    #page.window_frameless = True
    #page.window_title_bar_hidden = True
    #page.bgcolor = ft.colors.TRANSPARENT
    body = Contenedor()
    page.add(
            body
        )

ft.app(target=main)