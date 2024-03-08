import flet as ft


class Dashboard(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/dashboard")
        self.page = page
        #  the navigation for the system will be here ==== //
        self.navigation_rail = ft.NavigationRail(

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
