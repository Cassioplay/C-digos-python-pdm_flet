import flet as ft

def main(page: ft.Page):
    
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START

    coluna = ft.Column(
        controls=[
            ft.Container(width=75, height=75, bgcolor=ft.Colors.YELLOW),
            ft.Container(width=75, height=75, bgcolor=ft.Colors.GREEN),
            ft.Container(width=75, height=75, bgcolor=ft.Colors.BLUE),
        ]
    )

    def mudar_alinhamento(e):
        opcao = e.control.content.value

        if opcao == "Início e Início":
            page.horizontal_alignment = ft.CrossAxisAlignment.START
            page.vertical_alignment = ft.MainAxisAlignment.START

        elif opcao == "Início e Centro":
            page.horizontal_alignment = ft.CrossAxisAlignment.START
            page.vertical_alignment = ft.MainAxisAlignment.CENTER

        elif opcao == "Início e Fim":
            page.horizontal_alignment = ft.CrossAxisAlignment.START
            page.vertical_alignment = ft.MainAxisAlignment.END

        elif opcao == "Centro e Início":
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.vertical_alignment = ft.MainAxisAlignment.START

        elif opcao == "Centro e Centro":
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.vertical_alignment = ft.MainAxisAlignment.CENTER

        elif opcao == "Centro e Fim":
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.vertical_alignment = ft.MainAxisAlignment.END

        elif opcao == "Fim e Início":
            page.horizontal_alignment = ft.CrossAxisAlignment.END
            page.vertical_alignment = ft.MainAxisAlignment.START

        elif opcao == "Fim e Centro":
            page.horizontal_alignment = ft.CrossAxisAlignment.END
            page.vertical_alignment = ft.MainAxisAlignment.CENTER

        elif opcao == "Fim e Fim":
            page.horizontal_alignment = ft.CrossAxisAlignment.END
            page.vertical_alignment = ft.MainAxisAlignment.END

        page.update()

    menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(content=ft.Text("Início e Início"), on_click=mudar_alinhamento),
            ft.PopupMenuItem(content=ft.Text("Início e Centro"), on_click=mudar_alinhamento),
            ft.PopupMenuItem(content=ft.Text("Início e Fim"), on_click=mudar_alinhamento),
            ft.PopupMenuItem(content=ft.Text("Centro e Início"), on_click=mudar_alinhamento),
            ft.PopupMenuItem(content=ft.Text("Centro e Centro"), on_click=mudar_alinhamento),
            ft.PopupMenuItem(content=ft.Text("Centro e Fim"), on_click=mudar_alinhamento),
            ft.PopupMenuItem(content=ft.Text("Fim e Início"), on_click=mudar_alinhamento),
            ft.PopupMenuItem(content=ft.Text("Fim e Centro"), on_click=mudar_alinhamento),
            ft.PopupMenuItem(content=ft.Text("Fim e Fim"), on_click=mudar_alinhamento),
        ]
    )

    page.add(menu, coluna)

ft.app(target=main)