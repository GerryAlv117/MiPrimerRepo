import flet as ft

def main(page: ft.Page):
   
    page.bgcolor = ft.Colors.BLACK
    page.title = "Enciclopedia de Gamer"
    page.scroll=True
    modo_inicio = True
    titulo = ft.Text("Bienvenido a la Enciclopedia Gamer", size=30, color=ft.Colors.WHITE)


    imagen_portada = ft.Image(
        src="https://www.elinformador.com.co/images/stories/general/2017/06-junio/20entre6.jpg",
        width=600,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )


    halo_logo = ft.Image(
        src="https://wallpaperaccess.com/full/50036.jpg",
        width=600,
        height=200,
        fit=ft.ImageFit.COVER,
    )


    inicio_container = ft.Container(
        content=ft.Column(
            [titulo, imagen_portada],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
    )


    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Inicio",
                content=ft.Column([
                    ft.ElevatedButton("Volver a pantalla de inicio", on_click=lambda e: mostrar_pantalla_inicio())
                ])
            ),

            ft.Tab(text="Personajes", content=ft.Text("Contenido de Personajes")),  
            ft.Tab(text="Armas", content=ft.Text("Contenido de Armas")),
            ft.Tab(text="Vehiculos", content=ft.Text("Contenido de Vehiculos")),
            ft.Tab(text="Naves", content=ft.Text("Contenido de Naves")),
            ft.Tab(text="Quiz", content=ft.Text("Contenido de Quiz")),
        ],
        expand=1
    )


    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Buscar"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Configuración")
        ],
        on_change=lambda e: cambiar_pagina(int(e.data))
    )


    def cambiar_pagina(index):

        if modo_inicio:
            return

        page.clean()
        page.add(page.navigation_bar)

        if index ==0:

            page.add(
                ft.Column(
                    [
                        titulo, imagen_portada, tabs,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

        elif index == 1:

            search_container = ft.Container(
                content=ft.Column(
                    [ft.TextField(label="Buscar"), ft.ElevatedButton("Buscar")],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=20,
                bgcolor=ft.Colors.WHITE,
            )
            page.add(search_container)

        elif index == 2:

            config_container = ft.Container(
                content=ft.Column(
                    [ft.TextField("Ajustes"), ft.Slider(value=50, min=0, max=100)],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=20,
                bgcolor=ft.Colors.WHITE,
            )
            page.add(config_container)
        page.update()


    def alternar_inicio():
        nonlocal modo_inicio
        modo_inicio = False
        page.clean()
        page.add(page.navigation_bar)
        page.add(ft.Column(
            [titulo, imagen_portada, tabs],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ))
        page.update()


    def boton_principal_inicio():

        return ft.ElevatedButton(
            "Entrar",
            on_click = lambda e: alternar_inicio(),
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.HOVERED: ft.Colors.WHITE,
                    ft.ControlState.DEFAULT: ft.Colors.BLUE,
                    ft.ControlState.FOCUSED: ft.Colors.BLACK,
                },
                bgcolor={ft.ControlState.FOCUSED: ft.Colors.PINK_200, "": ft.Colors.BLUE},
                padding={ft.ControlState.HOVERED: 20},
                overlay_color=ft.Colors.TRANSPARENT,
                elevation={ft.ControlState.PRESSED: 0,
                            ft.ControlState.DEFAULT: 1},
                animation_duration=500,
                side={
                    ft.ControlState.DEFAULT: ft.BorderSide(2, ft.Colors.WHITE),
                    ft.ControlState.HOVERED: ft.BorderSide(2, ft.Colors.BLUE),
                },
                shape={
                    ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                    ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
                },
            ),
        )


    def mostrar_pantalla_inicio():
        nonlocal modo_inicio
        modo_inicio = True

        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Row(
                    [halo_logo,
                    boton_principal_inicio()],
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()
    
    mostrar_pantalla_inicio()

ft.app(target=main)