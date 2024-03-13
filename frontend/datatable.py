from flet import *
import sqlite3
from PIL import Image

conn=sqlite3.connect('db/dbcat.db', check_same_thread=False)

tb=DataTable(
    columns=[
        DataColumn(Text('Acciones')),
        DataColumn(Text('id_almacen')),
        DataColumn(Text('id_proveedor')),
        DataColumn(Text('descripcion')),
        DataColumn(Text('grupo')),
        DataColumn(Text('subgrupo')),
        DataColumn(Text('unidad')),
        DataColumn(Text('proveedor')),
        DataColumn(Text('partida_presupuestaria')),
        DataColumn(Text('precio_unitario')),
        DataColumn(Text('precio_historico')),
        DataColumn(Text('precio_usd')),
        DataColumn(Text('id_anterior ')),
        DataColumn(Text('imagen')),
        DataColumn(Text('plano')),
        DataColumn(Text('posicion_plano')),
        DataColumn(Text('id_plano')),
        DataColumn(Text('trabajo')),
        DataColumn(Text('ubicacion')),
        DataColumn(Text('recurrencia')),
        DataColumn(Text('observaciones')),
    ],
    rows=[]
)

def showdelete(e):
    try:
        myid = int(e.control.data)
        c = conn.cursor()
        c.execute("DELETE FROM catalogo WHERE id=?",(myid,))
        conn.commit()
        tb.rows.clear()
        calldb()
        tb.update()

    except Exception as erro:
        print(erro)

id_edit = Text()
idA_edit = TextField(label='id_almacen')
idP_edit = TextField(label='id_proveedor')
des_edit = TextField(label='descripcion')
gru_edit = TextField(label='grupo')
sub_edit = TextField(label='subgrupo')
und_edit = TextField(label='unidad')
pro_edit = TextField(label='proveedor')
ppa_edit = TextField(label='partida_presupuestaria')
puo_edit = TextField(label='precio_unitario')
pho_edit = TextField(label='precio_historico')
pud_edit = TextField(label='precio_usd')
ant_edit = TextField(label='id_anterior')
img_edit = TextField(label='imagen')
pla_edit = TextField(label='plano')
ppl_edit = TextField(label='posicion_plano')
ipl_edit = TextField(label='id_plano')
tbj_edit = TextField(label='trabajo')
ubc_edit = TextField(label='ubicacion')
rcr_edit = TextField(label='recurrencia')
obs_edit = TextField(label='observaciones')

id_view = Text()
idA_view = TextField(label='id_almacen')
idP_view = TextField(label='id_proveedor')
des_view = TextField(label='descripcion')
gru_view = TextField(label='grupo')
sub_view = TextField(label='subgrupo')
und_view = TextField(label='unidad')
pro_view = TextField(label='proveedor')
ppa_view = TextField(label='partida_presupuestaria')
puo_view = TextField(label='precio_unitario')
pho_view = TextField(label='precio_historico')
pud_view = TextField(label='precio_usd')
ant_view = TextField(label='id_anterior')
img_view = TextField(label='imagen')
pla_view = TextField(label='plano')
ppl_view = TextField(label='posicion_plano')
ipl_view = TextField(label='id_plano')
tbj_view = TextField(label='trabajo')
ubc_view = TextField(label='ubicacion')
rcr_view = TextField(label='recurrencia')
obs_view = TextField(label='observaciones')

def hidedlg(e):
    dlg.visible=False
    dlg.update()

def hidedlgv(e):
    view_dlg.visible=False
    view_dlg.update()

def updateandsave(e):
    try:
        myid = id_edit.value
        c=conn.cursor()
        c.execute(
            """UPDATE catalogo SET id_almacen=?, id_proveedor=?,descripcion=?, grupo=?, subgrupo=?, unidad=?,
            proveedor=?, partida_presupuestaria=?,precio_unitario=?, precio_historico=?, precio_usd=?, id_anterior=?,
            imagen=?, plano=?,posicion_plano=?, id_plano=?, trabajo=?, ubicacion=?,recurrencia=?, observaciones=?
            WHERE id=?""", (idA_edit.value, idP_edit.value, des_edit.value, gru_edit.value, sub_edit.value, und_edit.value, 
            pro_edit.value, ppa_edit.value, puo_edit.value, pho_edit.value, pud_edit.value, ant_edit.value,
            img_edit.value, pla_edit.value, ppl_edit.value, ipl_edit.value, tbj_edit.value, ubc_edit.value,rcr_edit.value, 
            obs_edit.value, myid)
        )
        conn.commit()
        print('Editado con éxito')
        tb.rows.clear()
        calldb()
        dlg.visible=False
        dlg.update()
        tb.update()

    except Exception as erro:
        print('El error está aquí', erro)

dlg = Container(
    bgcolor='green200',
    padding=10,
    content=Column([
        Row([
            Text(
                'Editar datos',
                size=20,
                weight='bold'
            ),
            IconButton(
                icon='close', 
                on_click=hidedlg
            )], alignment='spaceBetween'),
        idA_edit, idP_edit, des_edit, gru_edit, sub_edit, und_edit, 
        pro_edit, ppa_edit, puo_edit, pho_edit, pud_edit, ant_edit,
        img_edit, pla_edit, ppl_edit, ipl_edit, tbj_edit, ubc_edit,rcr_edit, 
        obs_edit,
        ElevatedButton(
            'Actualizar',
            on_click=updateandsave
        ),
    ])
)

def showedit(e):
    data_edit = e.control.data
    id_edit.value = data_edit['id']
    idA_edit.value = data_edit['id_almacen']
    idP_edit.value = data_edit['id_proveedor']
    des_edit.value = data_edit['descripcion']
    gru_edit.value = data_edit['grupo']
    sub_edit.value = data_edit['subgrupo']
    und_edit.value = data_edit['unidad']
    pro_edit.value = data_edit['proveedor']
    ppa_edit.value = data_edit['partida_presupuestaria']
    puo_edit.value = data_edit['precio_unitario']
    pho_edit.value = data_edit['precio_historico']
    pud_edit.value = data_edit['precio_usd']
    ant_edit.value = data_edit['id_anterior']
    img_edit.value = data_edit['imagen']
    pla_edit.value = data_edit['plano']
    ppl_edit.value = data_edit['posicion_plano']
    ipl_edit.value = data_edit['id_plano']
    tbj_edit.value = data_edit['trabajo']
    ubc_edit.value = data_edit['ubicacion']
    rcr_edit.value = data_edit['recurrencia']
    obs_edit.value = data_edit['observaciones']

    dlg.visible=True
    dlg.update()

view_dlg = Container(
    bgcolor='green200',
    padding=10,
    content=Column([
        Row([
            Text(
                'Ver datos',
                size=20,
                weight='bold'
            ),
            IconButton(
                icon='close', 
                on_click=hidedlgv
            )], alignment='spaceBetween'),
        id_view, idA_view, idP_view, des_view, gru_view, sub_view, und_view, 
        pro_view, ppa_view, puo_view, pho_view, pud_view, ant_view,
        img_view, pla_view, ppl_view, ipl_view, tbj_view, ubc_view,rcr_view, 
        obs_view,
    ])
)
def showview(e):
    data_view = e.control.data
    id_view.value = data_view['id']
    idA_view.value = data_view['id_almacen']
    idP_view.value = data_view['id_proveedor']
    des_view.value = data_view['descripcion']
    gru_view.value = data_view['grupo']
    sub_view.value = data_view['subgrupo']
    und_view.value = data_view['unidad']
    pro_view.value = data_view['proveedor']
    ppa_view.value = data_view['partida_presupuestaria']
    puo_view.value = data_view['precio_unitario']
    pho_view.value = data_view['precio_historico']
    pud_view.value = data_view['precio_usd']
    ant_view.value = data_view['id_anterior']
    img_view.value = data_view['imagen']
    pla_view.value = data_view['plano']
    ppl_view.value = data_view['posicion_plano']
    ipl_view.value = data_view['id_plano']
    tbj_view.value = data_view['trabajo']
    ubc_view.value = data_view['ubicacion']
    rcr_view.value = data_view['recurrencia']
    obs_view.value = data_view['observaciones']

    view_dlg.visible=True
    view_dlg.update()

def calldb(search_value=None):  # Añade un parámetro opcional para el valor de búsqueda
    c = conn.cursor()
    if search_value:  # Si se proporciona un valor de búsqueda
        # Consulta SQL con una cláusula WHERE para filtrar los resultados por ID, id_proveedor, id_almacen o descripcion
        c.execute("""SELECT * FROM catalogo WHERE id_proveedor=? OR id_almacen=? OR descripcion=?""", (search_value, search_value, search_value))
    else:
        c.execute('SELECT * FROM catalogo')
    catalogo = c.fetchall()
    print(catalogo)

    if not catalogo == '':
        keys= ['id', 'id_almacen', 'id_proveedor', 'descripcion', 'grupo', 'subgrupo', 'unidad','proveedor', 
            'partida_presupuestaria', 'precio_unitario', 'precio_historico', 'precio_usd', 'id_anterior', 
            'imagen','plano', 'posicion_plano', 'id_plano', 'trabajo', 'ubicacion', 'recurrencia', 'observaciones']
        result = [dict(zip(keys, values)) for values in catalogo]
        for x in result:
            tb.rows.append(
                DataRow(
                    cells=[
                        DataCell(
                            Row([
                                IconButton(
                                    icon='create',
                                    icon_color='blue',
                                    data=x,
                                    on_click=showedit
                                ),
                                IconButton(
                                    icon='delete',
                                    icon_color='red',
                                    data=x['id'],
                                    on_click=showdelete
                                ),
                                IconButton(
                                    icon='visibility',
                                    icon_color='green',
                                    data=x,
                                    on_click=showview
                                ),
                            ])
                        ),
                        DataCell(Text(x['id_almacen'])),
                        DataCell(Text(x['id_proveedor'])),
                        DataCell(Text(x['descripcion'])),
                        DataCell(Text(x['grupo'])),
                        DataCell(Text(x['subgrupo'])),
                        DataCell(Text(x['unidad'])),
                        DataCell(Text(x['proveedor'])),
                        DataCell(Text(x['partida_presupuestaria'])),
                        DataCell(Text(x['precio_unitario'])),
                        DataCell(Text(x['precio_historico'])),
                        DataCell(Text(x['precio_usd'])),
                        DataCell(Text(x['id_anterior'])),
                        DataCell(Text(x['imagen'])),
                        DataCell(Text(x['plano'])),
                        DataCell(Text(x['posicion_plano'])),
                        DataCell(Text(x['id_plano'])),
                        DataCell(Text(x['trabajo'])),
                        DataCell(Text(x['ubicacion'])),
                        DataCell(Text(x['recurrencia'])),
                        DataCell(Text(x['observaciones'])),
                    ],
                ),
            )

calldb()
dlg.visible=False
view_dlg.visible=False

mytable = Column([
    dlg,view_dlg,
    Row([tb],scroll='always')
])