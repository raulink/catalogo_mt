from flet import *
import flet as ft
# import sqlite3

import requests

tb = DataTable(
    columns=[
        DataColumn(Text("Acciones")),
        DataColumn(Text("Descripcion")),
        DataColumn(Text("Categoria")),
        DataColumn(Text("Rating")),
        DataColumn(Text("Titulo")),
        DataColumn(Text("Año")),
    ],
    rows=[]
)


def showdelete(e):
    """Deletes a movie using the provided ID and updates the table."""
    try:
        myid = int(e.control.data)

        # Send DELETE request to the API
        url = f"http://127.0.0.1:8000/movies/{myid}"
        response = requests.delete(url)
        response.raise_for_status()  # Raise exception for error responses

        print("Movie deleted successfully!")

        # Clear existing rows and fetch data again
        tb.rows.clear()
        call_api()
        tb.update()

    except requests.exceptions.RequestException as err:
        print(f"Error deleting movie (ID: {myid}): {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


id_edit = Text()
overview_edit = TextField(label="Overview")
category_edit = TextField(label="Category")
rating_edit = TextField(label="Rating")
title_edit = TextField(label="Title")
year_edit = TextField(label="Year")

# Ocultar datos edicion


def hidedlg(e):
    dlg.visible = False
    dlg.update()


def updateandsave(e):
    try:
        myid = id_edit.value

        # Gather updated data from fields
        data = {
            "id": myid,  # Ensure ID is included in the request body
            "title": title_edit.value,
            "overview": overview_edit.value,
            "year": year_edit.value,
            "rating": rating_edit.value,
            "category": category_edit.value
        }

        # Send PUT request to API
        url = f"http://127.0.0.1:8000/movies/{myid}"
        response = requests.put(url, json=data)
        response.raise_for_status()  # Raise exception for error responses

        print("Movie updated successfully!")

        # Clear existing rows and fetch data again
        tb.rows.clear()
        call_api()
        dlg.visible = False
        dlg.update()
        tb.update()

    except requests.exceptions.RequestException as err:
        print(f"Error updating movie (ID: {myid}): {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


dlg = Container(
    # bgcolor="blue200",
    bgcolor=ft.colors.BLUE_ACCENT,
    padding=10,
    content=Column([
        Row([
            Text("Formulario de edicion", size=30, weight="bold"),
            IconButton(icon="close", on_click=hidedlg),
        ]),#, alignment="spaceBetween"
        id_edit,
        overview_edit,
        category_edit,
        rating_edit,
        title_edit,
        year_edit,

        ElevatedButton("Actualizar", on_click=updateandsave)
    ])
)

# Mostrar datos de edicion
def showedit(e):
    data_edit = e.control.data
    id_edit.value = data_edit['id']
    title_edit.value = data_edit['title']
    overview_edit.value = data_edit['overview']
    year_edit.value = data_edit['year']
    rating_edit.value = data_edit['rating']
    category_edit.value = data_edit['category']

    dlg.visible = True
    dlg.update()

# Obtener datos de la base de datos
def call_api():
    """Sends a request to the API and processes the response."""

    try:
        response = requests.get("http://127.0.0.1:8000/movies")
        response.raise_for_status()  # Raise an exception for error responses

        movies = response.json()  # Assuming the API response is in JSON format
        print(movies)

        if movies:
            #keys = ['id', 'overview', 'category', 'rating', 'title', 'year']
            #result = [dict(zip(keys, values)) for values in movies]
            for x in movies:
                print (x)
                tb.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Row([
                                IconButton(icon="create", icon_color="blue",
                                           data=x,
                                           on_click=showedit
                                           ),
                                IconButton(icon="delete", icon_color="red",
                                           data=x['id'],
                                           on_click=showdelete

                                           ),
                            ])),
                            #DataCell(Text(x['id'])),
                            DataCell(Text(x['overview'])),
                            DataCell(Text(x['category'])),
                            DataCell(Text(x['rating'])),
                            DataCell(Text(x['title'])),
                            DataCell(Text(x['year'])),
                        ],
                    ),

                )

    except requests.exceptions.RequestException as err:
        print("Error fetching data from API:", err)
        # Handle the error gracefully, e.g., display an error message


call_api()


dlg.visible = False
mytable = Column([
    dlg,
    Row([tb], scroll="always")
])
