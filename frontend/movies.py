import json
import flet as ft
import requests

class Categorias:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
    @classmethod
    def from_json(cls,json_data):
        return Categorias(json_data['id'],json_data['nombre']) 

def main(page:ft.Page):
    #page.window_title_bar_hidden = True
    #page.window_title_bar_buttons_hidden = True

    # Crea los campos del formulario    
    title = ft.TextField(label="Titulo",max_length=20)
    overview = ft.TextField(label="Descripción",max_length=20)    
    year = ft.TextField(label="Año")    
    rating = ft.TextField(label="Rating")    
    category=ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Accion"),
            ft.dropdown.Option("Romantica"),
            ft.dropdown.Option("Triller"),
        ],
    )    

    # Crea un botón para enviar el formulario
    boton_enviar = ft.ElevatedButton(text="Enviar")
    

    def on_click(e):
        # Obtiene los valores de los campos del formulario
        datos =  {            
            "title": title.value,
            "overview": overview.value,
            "year": year.value,
            "rating": rating.value,
            "category": category.value
        }
        #datos = {'title': 'Mi película 3', 'overview': 'Descripción de la película', 'year': 2022, 'rating': 5.2, 'category': 'Acción'}
        #datos = {"title": "asdfqweasdfasd r", "overview": "asdfasdfasd", "year": 2000, "rating": 6.2, "category": "Triller"}

        # Convierte los datos a JSON
        #json_data = json.dumps(datos)        
        url = "http://localhost:8000/movies"

        # Envía los datos al API        
        headers = {'Content-Type': 'application/json'}
        print("Depuracion:")
        print(json.dumps(datos))
        response = requests.post(url, data=json.dumps(datos), headers=headers)        
        
        if response.status_code == 201:
            print("La solicitud POST fue exitosa.")
            print(response.text)
        else:            
            print(f"Error en la solicitud POST: {response.status_code}")            
            print(response.text)


        

    # Asigna la función al evento "click" del botón
    boton_enviar.on_click = on_click

    # Crea la ventana principal de la aplicación
    page.add(        
            ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            height=page.height-50,
            width=page.width,
            scroll=ft.ScrollMode.ALWAYS,
            controls=[
                title,
                overview ,
                year,
                rating ,    
                category,
                # Boton de accion
                boton_enviar,
            ]
        ), 
    )
ft.app(target=main)
