import json
import flet as ft

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
    id_field = ft.TextField(label="ID", max_length=255)
    descripcion_field = ft.TextField(label="Descripción", max_length=255)
    id_proveedor = ft.TextField(label="Proveedor",max_length=20)    
    id_almacen: str="1"
    precio_unitario=ft.TextField(
        label="Precio Unitario",        
        keyboard_type=ft.KeyboardType.NUMBER
    )       
    precio_unitario_historico= ft.TextField(
        label="Precio Unitario",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    
    unidad = ft.TextField(
        label="Unidad de medida"        
    )  # Unidad de medida del producto
    grupo = ft.TextField(
        label="Grupo"        
    )   # Grupo al que pertenece el producto
    sub_grupo= ft.TextField(
        label="Sub grupo"        
    )   # Subgrupo al que pertenece el producto
    partida_presupuestaria= ft.TextField(
        label="Partida Presupuestaria"        
    )   # Partida presupuestaria asociada al producto
    proveedor= ft.TextField(
        label="Proveedor"        
    )   # Nombre del proveedor
    imagen= ft.TextField(
        label="Imagen"        
    )   # Ruta de la imagen del producto
    plano= ft.TextField(
        label="Plano"        
    )   # Plano donde se encuentra el producto
    posicion_plano= ft.TextField(
        label="Posicion del plano"        
    )   # Posición del producto en el plano
    id_plano= ft.TextField(
        label="Id del plano"        
    )   # Identificador del plano
    ubicacion = ft.TextField(
        label="Ubicacion"        
    )    # Ubicación física del producto
    trabajo= ft.TextField(
        label="Trabajo"        
    )    # Trabajo asociado al producto
    recurrencia= ft.TextField(
        label="Recurrencia"        
    )    # Recurrencia del producto
    observaciones= ft.TextField(
        label="Observaciones"        
    )    # Observaciones adicionales del producto

    # ... (Agrega campos para cada uno de los atributos del modelo) ...

    # Crea un botón para enviar el formulario
    boton_enviar = ft.ElevatedButton(text="Enviar")
    

    def on_click(e):
        # Obtiene los valores de los campos del formulario
        datos = {
            "id": id_field.value,
            "descripcion": descripcion_field.value,
            "id_proveedor":id_proveedor.value,                
            "precio_unitario":precio_unitario.value,
            "precio_unitario_historico":precio_unitario_historico.value,                
            "unidad":unidad.value,
            "grupo":grupo.value,
            "sub_grupo":sub_grupo.value,
            "partida_presupuestaria":partida_presupuestaria.value,
            "proveedor":proveedor.value,
            "imagen":imagen.value,
            "plano":plano.value,
            "posicion_plano":posicion_plano.value,
            "id_plano":id_plano.value,
            "ubicacion":ubicacion.value,
            "trabajo":trabajo.value,
            "recurrencia":recurrencia.value,
            "observaciones":observaciones.value,            
        }

        # Convierte los datos a JSON
        json_data = json.dumps(datos)        

        # Envía los datos al API
        ft.http.post(
            url="http://localhost:8000/catalogo",
            data=json_data,
            headers={"Content-Type": "application/json"},
        )

        # Muestra un mensaje de éxito
        ft.alert(message="Datos enviados correctamente")

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
                    id_field,
                    descripcion_field,
                    # Campos de registro
                    id_proveedor,
                    precio_unitario,
                    precio_unitario_historico,                
                    unidad,
                    grupo,
                    sub_grupo,
                    partida_presupuestaria,
                    proveedor,
                    imagen,
                    plano,
                    posicion_plano,
                    id_plano,
                    ubicacion,
                    trabajo,
                    recurrencia,
                    observaciones,
                    # Boton de accion
                    boton_enviar,
                ]
            ), 
    )



ft.app(target=main)
