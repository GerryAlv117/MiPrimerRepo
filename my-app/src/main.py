import flet as ft


def main(page: ft.Page):
   
    page.bgcolor = ft.colors.BLUE_GREY_50
    page.title = "Enciclopedia de Gamer"
    page.scroll=True

    titulo = ft.Text(
        "Bienvenido a la Enciclopedia Gamer", size=30, color=ft.colors.BLACK
    )

    imagen_portada = ft.Image(
        src="https://images.hdqwalls.com/wallpapers/halo-reach-3p.jpg",
        width=600,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Inicio",content=ft.Text("Contenido de Inicio")),
            ft.Tab(text="Personajes", content=ft.Text("Contenido de Personajes")),  
            ft.Tab(text="Armas", content=ft.Text("Contenido de Armas")),
            ft.Tab(text="Vehiculos", content=ft.Text("Contenido de Vehiculos")),
            ft.Tab(text="Naves", content=ft.Text("Contenido de Naves")),
            ft.Tab(text="Quiz", content=ft.Text("Contenido de Quiz")),
        ],
        expand=1
    )


    page.add(
        ft.Column(
            [
                titulo, 
                imagen_portada,
                tabs
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)