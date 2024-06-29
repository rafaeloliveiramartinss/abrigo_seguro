import sys
import os
import flet as ft

# Adiciona o diretório raiz ao caminho do Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from app.views.main_view import main_view

def main(page: ft.Page):
    page.title = "Abrigo Seguro"
    page.theme = ft.Theme(color_scheme_seed=ft.colors.DEEP_PURPLE)
    page.padding = 16
    page.bgcolor = ft.colors.PURPLE_900
    main_view(page)

if __name__ == "__main__":
    ft.app(target=main)
