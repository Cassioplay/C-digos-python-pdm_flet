import flet as ft

def main(page: ft.Page):
   
    page.theme_mode = ft.ThemeMode.LIGHT

    texto = ft.Text("Claro")

    def mudar_tema(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            texto.value = "Escuro"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            texto.value = "Claro"

        page.update()
    botao = ft.ElevatedButton("Mudar tema", on_click=mudar_tema)

    page.add(botao,texto )

ft.app(target=main)