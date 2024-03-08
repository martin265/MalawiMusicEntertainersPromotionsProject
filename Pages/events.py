import flet as ft


class EventsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        # ========= the user controls will be here ====== //
        self.content = ft.Container(
            content=ft.SafeArea(
                content=ft.ResponsiveRow(
                    #  ======== the first container for the events details will be here ========= //
                    [
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    # ======== the container for the top information
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    controls=[
                                                        ft.Icon(
                                                            ft.icons.EVENT_NOTE_ROUNDED,
                                                            size=60,
                                                            color="#212121"
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            gradient=ft.LinearGradient(
                                colors=[
                                    "#CBCCFF",
                                    "#CBCCFF"
                                ],
                                begin=ft.alignment.center_left,
                                end=ft.alignment.top_right
                            ),
                            border_radius=ft.border_radius.all(10),
                            col={"sm": 12, "md": 9, "lg": 9}
                        ),

                        ft.Container(
                            content=ft.Text("hello"),
                            height=300,
                            bgcolor="yellow",
                            col={"sm": 12, "md": 3, "lg": 3}
                        ),
                    ]
                )
            )
        )