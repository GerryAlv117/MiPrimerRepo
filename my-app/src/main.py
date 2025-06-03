import flet as ft

def main(page: ft.Page):
   
    page.bgcolor = ft.Colors.BLACK
    page.title = "Enciclopedia de Gamer"
    page.scroll=True
    titulo = ft.Text(
        "Bienvenido a la Enciclopedia Gamer", size=30, color=ft.Colors.WHITE
    )

    imagen_portada = ft.Image(
        src="https://www.elinformador.com.co/images/stories/general/2017/06-junio/20entre6.jpg",
        width=600,
        height=200,
        fit=ft.ImageFit.CONTAIN,
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
            ft.Tab(text="Inicio",content=inicio_container),

            ft.Tab(text="Personajes", content=ft.Text("Contenido de Personajes")),  
            ft.Tab(text="Armas", content=ft.Text("Contenido de Armas")),
            ft.Tab(text="Vehiculos", content=ft.Text("Contenido de Vehiculos")),
            ft.Tab(text="Naves", content=ft.Text("Contenido de Naves")),
            ft.Tab(text="Quiz", content=ft.Text("Contenido de Quiz")),
        ],
        expand=1
    )


    def cambiar_pagina(index):

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


    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Buscar"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Configuración")
        ],
        on_change=lambda e: cambiar_pagina(int(e.data))
    )


    page.add(
        ft.Column(
            [
                titulo, 
                imagen_portada,
                tabs,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)