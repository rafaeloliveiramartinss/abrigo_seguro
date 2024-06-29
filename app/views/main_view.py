import flet as ft

def main(page: ft.Page):
    def on_login_click(e):
        # Lógica de autenticação aqui
        pass

    email_input = ft.TextField(label="E-mail/Username", width=300)
    password_input = ft.TextField(label="Senha", password=True, width=300)

    login_button = ft.ElevatedButton(
        text="ENTRAR",
        on_click=on_login_click,
        style=ft.ButtonStyle(
            bgcolor=ft.LinearGradient(colors=[ft.colors.RED, ft.colors.PURPLE]),
            color=ft.colors.WHITE,
        ),
        width=300
    )

    page.add(
        ft.Column(
            [
                ft.Image(src="app/assets/icons/logo.png", height=100),
                ft.Text(
                    "Seja bem-vinda ao",
                    style=ft.TextStyle(size=24, color=ft.colors.WHITE)
                ),
                ft.Text(
                    "ABRIGO SEGURO",
                    style=ft.TextStyle(size=28, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)
                ),
                email_input,
                password_input,
                ft.Row(
                    [
                        ft.Checkbox(),
                        ft.Text("Lembrar-me", color=ft.colors.WHITE),
                        ft.Text("Esqueceu a senha?", color=ft.colors.WHITE)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    width=300
                ),
                login_button,
                ft.Text(
                    "REALIZAR CADASTRO",
                    style=ft.TextStyle(color=ft.colors.WHITE, decoration=ft.TextDecoration.UNDERLINE)
                ),
                ft.Row(
                    [
                        ft.CircleAvatar(
                            radius=30,
                            content=ft.Image(src="app/assets/icons/help_icon.png", height=40)
                        ),
                        ft.Text("Precisa de ajuda?", color=ft.colors.WHITE)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)
