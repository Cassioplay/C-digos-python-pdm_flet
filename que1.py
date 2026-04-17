import flet as ft


def main(page: ft.Page): 
    nome_input = ft.TextField(label="Digite seu nome... ")
    resultado = ft.Text()

    def enviar(e):
        nome = nome_input.value
        resultado.value = f"Olá¡, {nome}!"
        page.update()

    botao = ft.ElevatedButton("Enviar", on_click=enviar)

    page.add(nome_input, botao, resultado)

    
ft.app(target=main)