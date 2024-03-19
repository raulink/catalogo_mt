import flet as ft


class Contenedor(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        self.visible = True
        return ft.Container(
            ft.Row([
                ft.Container(
                    ft.Column(controls=[
                        ft.Container(
                            ft.Image(
                                src='logo.png',
                                width=70,
                            ),
                            padding=ft.padding.only(150, 20)
                        ),
                        ft.Text(
                            'Iniciar Sesión',
                            width=360,
                            size=30,
                            weight='w900',
                            text_align='center'
                        ),
                        ft.Container(
                            ft.TextField(
                                width=280,
                                height=40,
                                hint_text='Correo electronico',
                                border='underline',
                                color='black',
                                prefix_icon=ft.icons.EMAIL,
                            ),
                            padding=ft.padding.only(20, 10)
                        ),
                        ft.Container(
                            ft.TextField(
                                width=280,
                                height=40,
                                hint_text='Contraseña',
                                border='underline',
                                color='black',
                                prefix_icon=ft.icons.LOCK,
                                password=True,
                            ),
                            padding=ft.padding.only(20, 10)
                        ),
                        ft.Container(
                            ft.Checkbox(
                                label='Recordar contraseña',
                                check_color='black'
                            ),
                            padding=ft.padding.only(40),
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                content=ft.Text(
                                    'INICIAR',
                                    color='white',
                                    weight='w500',
                                ),
                                width=280,
                                bgcolor='black',
                            ),
                            padding=ft.padding.only(25, 10)
                        ),
                        ft.Container(
                            ft.Row([
                                ft.Text(
                                    '¿No tiene una cuenta?'
                                ),
                                ft.TextButton(
                                    'Crear una cuenta'
                                ),
                            ], spacing=8),
                            padding=ft.padding.only(40)
                        ),
                    ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    ),
                    gradient=ft.LinearGradient(['red', 'orange']),
                    width=380,
                    height=460,
                    border_radius=20
                ),
            ],
            ),
            padding=20


        )
