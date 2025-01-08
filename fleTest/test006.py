import flet as ft

def main(page: ft.Page):
    print("Flet app started")  # Отладочный вывод
    page.title = "Debugging Flet"
    page.add(ft.Text("Привет, отладка!"))

ft.app(target=main, view=ft.WEB_BROWSER, port=8080)  # Убедитесь, что используется FLET_APP
