from flet import *
import flet as ft
# IMPORT YOU CREATE TABLE
#from myaction import create_table
from datatable import mytable, tb, call_api
import requests
#import sqlite3
#conn = sqlite3.connect("db/dbone.db", check_same_thread=False)


def main(page: Page):

    # AND RUN SCRIPT FOR CREATE TABLE WHEN FLET FIRST RUN
    # create_table()
    page.scroll = "auto"

    def showInput(e):
        inputcon.offset = transform.Offset(0, 0)
        page.update()

    def hidecon(e):
        inputcon.offset = transform.Offset(2, 0)
        page.update()
    
    # Nuevo Registro
    def savedata(e):
      try:
        # Gather data from input fields
        data = {
        "title": title.value,
        "overview": overview.value,  # Assuming "overview" field corresponds to "age" input (fix if different)
        "year": year.value,  # Assuming "year" field corresponds to "contact" input (fix if different)
        "rating": rating.value,  # Assuming "rating" field corresponds to "email" input (fix if different)
        "category": category.value,  # Assuming "category" field corresponds to "gender" input (fix if different)
        }

        # Send POST request to the API
        url = "http://127.0.0.1:8000/movies"
        print(data)
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise exception for error responses

        print("Movie saved successfully!")

        # Clear existing rows, fetch data again, update UI elements
        tb.rows.clear()
        call_api()
        inputcon.offset = transform.Offset(2, 0)
        page.snack_bar = SnackBar(Text("Data saved successfully"), bgcolor="green")
        page.snack_bar.open = True
        page.update()

      except requests.exceptions.RequestException as err:
        print(f"Error saving movie: {err}")
            # Handle the error gracefully, e.g., display an error message to the user
      except Exception as e:
        print(f"An unexpected error occurred: {e}")
    # Handle general exceptions
    # Handle exception appropriately, e.g., display an error message to the user

    # CREATE FIELD FOR INPUT

    title  = TextField(label="Titulo")
    overview = TextField(label="Descrpcion")
    year = TextField(label="Año")
    rating = TextField(label="Clasificacion")
    category = TextField(label="Categoria")    

    # CREATE MODAL INPUT FOR ADD NEW DATA
    inputcon = Card(
        # ADD SLIDE LEFT EFFECT
        offset=transform.Offset(2, 0),
        animate_offset=animation.Animation(600, curve="easeIn"),
        elevation=30,
        content=Container(
            content=Column([
                Row([
                    Text("Nuevo Registro", size=20, weight="bold"),
                    IconButton(icon="close", icon_size=30,
                               on_click=hidecon
                               ),
                ]),
                title,
                overview,
                year,
                rating,
                category,                
                FilledButton("Guardar Nuevo Registro",
                             on_click=savedata
                             )

            ])

        )

    )

    page.add(
        Column([
            Text("REGISTRO PELICULAS", size=30, weight="bold"),
            ElevatedButton("Añadir Registro",
                           on_click=showInput
                           ),
            mytable,
            # AND DIALOG FOR ADD DATA
            inputcon
            # NOTICE IF YOU ERROR
            # DISABLE import Datatable like this
        ])

    )


ft.app(target=main)
