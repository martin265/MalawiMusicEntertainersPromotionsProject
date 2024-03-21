import flet as ft


class Records(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  =========== the content for the page will be here ========== //
        self.content = ft.Column(
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            expand=True,
                            gradient=ft.LinearGradient(
                                colors=[
                                    "#CBCCFF",
                                    "#CBCCFF"
                                ],
                                begin=ft.alignment.top_right,
                                end=ft.alignment.bottom_left,
                            ),
                            border_radius=ft.border_radius.all(10),
                            content=ft.Container(
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Container(
                                            content=ft.Text("hello world"),
                                            col={"sm": 12, "md": 12, "lg": 4}
                                        ),
                                        ft.Container(
                                            content=ft.Text("hello world"),
                                            col={"sm": 12, "md": 12, "lg": 4}
                                        ),
                                        ft.Container(
                                            content=ft.Text("hello world"),
                                            col={"sm": 12, "md": 12, "lg": 4}
                                        ),

                                    ]
                                )
                            )
                        )
                    ]
                )
            ]
        )

