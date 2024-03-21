import flet as ft


class Records(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

