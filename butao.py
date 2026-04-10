import flet as ft

def main(page: ft.Page):
    page.title = "Mudar tema de Tema"

    page.theme_mode = ft.ThemeMode.LIGHT


    def trocar_tema(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    botao = ft.ElevatedButton("Mudar tema", on_click=trocar_tema)

    page.add(botao)

ft.app(target=main)