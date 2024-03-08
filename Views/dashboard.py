import flet as ft


class Dashboard(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/dashboard")
        self.page = page
        #  the navigation for the system will be here ==== //
        self.navigation_rail = ft.NavigationRail(
            leading=ft.FloatingActionButton(
                content=ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(
                                ft.icons.MUSIC_NOTE_ROUNDED,
                                size=30
                            )
                        ]
                    )
                )
            )
        )
        #  ========== returning the controls here
        self.controls = [
            ft.SafeArea(
                content=ft.Container(
                    content=ft.Text(
                        "hello",
                        color="black"
                    )
                )
            )
        ]
