import flet as ft


class Tickets(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  ========= the content for the tickets page will be here ==== //
        self.content = ft.Column(
            controls=[
                ft.SafeArea(
                    content=ft.ResponsiveRow(
                        controls=[
                            #  ========== the container for the form here
                            ft.Container(
                                content=ft.Column(
                                    controls=[

                                    ]
                                ),
                                col={"sm": 12, "md": 9, "lg": 8}
                            ),
                            #  =========== the container for the other tools
                            ft.Container(
                                content=ft.Column(
                                    controls=[

                                    ]
                                ),
                                col={"sm": 12, "md": 9, "lg": 4}
                            )
                        ]
                    )
                )
            ]
        )