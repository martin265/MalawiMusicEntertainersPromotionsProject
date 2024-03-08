import flet as ft


class EventsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        # ========= the user controls will be here ====== //
        self.controls = [
            ft.SafeArea(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            #  ========= responsive row for the containers
                            ft.ResponsiveRow(
                                [
                                    ft.Container(
                                        bgcolor="blue",
                                        height=200,
                                        col={"sm": 12, "md": 12, "lg": 9}
                                    ),
                                    ft.Container(
                                        bgcolor="black",
                                        height=200,
                                        col={"sm": 12, "md": 12, "lg": 3}
                                    )
                                ]
                            )
                        ]
                    )
                )
            )
        ]