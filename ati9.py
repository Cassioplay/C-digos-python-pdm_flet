import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    page.add(
        ft.Column(
            controls=[
                ft.Container(width=75, height=75, bgcolor=ft.Colors.YELLOW),
                ft.Container(width=75, height=75, bgcolor=ft.Colors.GREEN),
                ft.Container(width=75, height=75, bgcolor=ft.Colors.BLUE),
            ]
        )
    )

ft.app(target=main)