# Obtenido desde https://github.com/wesleyp846/Cadastro_com_flet

from flet import *
import flet as ft
from useraction_table import create_table
from datatable import mytable,tb,calldb
import sqlite3
from PIL import Image

conn=sqlite3.connect('db/dbcat.db', check_same_thread=False)

def main(page:Page):
    page.theme_mode='light'
    create_table()
    page.scroll = 'auto'

    def showinput(e):
        idA_crt.value="" 
        idP_crt.value=""
        des_crt.value=""
        gru_crt.value=""
        sub_crt.value=""
        und_crt.value=""
        pro_crt.value=""
        ppa_crt.value=""
        puo_crt.value=""
        pho_crt.value=""
        pud_crt.value=""
        ant_crt.value=""
        img_crt.value=""
        pla_crt.value=""
        ppl_crt.value=""
        ipl_crt.value=""
        tbj_crt.value=""
        ubc_crt.value=""
        rcr_crt.value=""
        obs_crt.value=""
        inputcon.offset=transform.Offset(0,0)
        page.update()

    def hidecon(e):
        inputcon.offset=transform.Offset(1,0)
        page.update()

    def savedata(e):
        try:
            img_path = f'assets/{img_crt.value.filename}'
            img_crt.value.save(img_path)
            c=conn.cursor()
            c.execute('''INSERT INTO catalogo (id_almacen, id_proveedor, descripcion, grupo, subgrupo, unidad, proveedor, 
                    partida_presupuestaria, precio_unitario, precio_historico,precio_usd, id_anterior, imagen, plano, 
                    posicion_plano, id_plano, trabajo, ubicacion, recurrencia, observaciones) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
                idA_crt.value, 
                idP_crt.value, 
                des_crt.value, 
                gru_crt.value, 
                sub_crt.value, 
                und_crt.value, 
                pro_crt.value, 
                ppa_crt.value, 
                puo_crt.value, 
                pho_crt.value, 
                pud_crt.value, 
                ant_crt.value,
                img_crt.value, 
                pla_crt.value, 
                ppl_crt.value, 
                ipl_crt.value, 
                tbj_crt.value, 
                ubc_crt.value,
                rcr_crt.value, 
                obs_crt.value)
            )
            conn.commit()
            print('success')

            inputcon.offset=transform.Offset(2,0)

            page.snack_bar  = SnackBar(
                Text('Registro exitoso'),
                bgcolor='green'
            )
            page.snack_bar.open=True
            tb.rows.clear()
            calldb()
            tb.update()
            page.update()

        except Exception as e:
            print('Se unió a def savedata(e): pero no se fue', e)

    idA_crt = TextField(label='id_almacen')
    idP_crt = TextField(label='id_proveedor')
    des_crt = TextField(label='descripcion')
    gru_crt = TextField(label='grupo')
    sub_crt = TextField(label='subgrupo')
    und_crt = TextField(label='unidad')
    pro_crt = TextField(label='proveedor')
    ppa_crt = TextField(label='partida_presupuestaria')
    puo_crt = TextField(label='precio_unitario')
    pho_crt = TextField(label='precio_historico')
    pud_crt = TextField(label='precio_usd')
    ant_crt = TextField(label='id_anterior')
    img_crt = TextField(label='imagen')
    pla_crt = TextField(label='plano')
    ppl_crt = TextField(label='posicion_plano')
    ipl_crt = TextField(label='id_plano')
    tbj_crt = TextField(label='trabajo')
    ubc_crt = TextField(label='ubicacion')
    rcr_crt = TextField(label='recurrencia')
    obs_crt = TextField(label='observaciones')

    inputcon = Card(
        offset=transform.Offset(2,0),
        animate_offset=animation.Animation(600,curve='easyIn'),
        elevation=30,
        content=Container(
            bgcolor='green200',
            content=Column([
                Row([
                    Text('Nuevo registro',size=20,weight='bold'),
                    IconButton(icon='close',icon_size=30, on_click=hidecon),
                ]),
                idA_crt, idP_crt, des_crt, gru_crt, sub_crt, und_crt, pro_crt, ppa_crt, puo_crt, pho_crt, pud_crt, 
                ant_crt,img_crt, pla_crt, ppl_crt, ipl_crt, tbj_crt, ubc_crt,rcr_crt, obs_crt,
                FilledButton('Salvar dados', on_click=savedata)
            ])
        )
    )
    search_input = TextField(label='Buscar por ID, id_proveedor, id_almacen o descripcion')

    def search_data(e):
        search_value = search_input.value.strip()  # Obtener el valor de búsqueda y eliminar los espacios en blanco al inicio y al final
        tb.rows.clear()  # Limpiar las filas de la tabla
        calldb(search_value)  # Llamar a la función calldb() con el valor de búsqueda como argumento
        inputcon.offset=transform.Offset(2,0)
        page.update()
        
    page.add(
        Column([
            Text('Registro de Catalogo', size=30, weight='bold'),
            Row([search_input, ElevatedButton('Buscar', on_click=search_data)]),  # Agrega el campo de búsqueda y el botón de búsqueda en una fila
            ElevatedButton('Registrar', on_click=showinput),
            mytable,
            inputcon
        ])
    )

ft.app(target=main)