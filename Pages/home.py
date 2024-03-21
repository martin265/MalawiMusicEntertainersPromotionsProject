import flet as ft


class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  ======== the fonts for the system will be here ======= //
        self.page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }
        #  =========== the content for the page will be here ========== //
        self.content = ft.Column(
            adaptive=True,
            controls=[
                ft.ResponsiveRow(
                    adaptive=True,
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
                                content=ft.Column(
                                    controls=[
                                        #  ========= the container for the
                                        ft.Container(
                                            content=ft.Column(
                                                controls=[
                                                    #  ========= container for the top text
                                                    ft.Container(
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Text(
                                                                    "home",
                                                                    font_family="manrop-bold",
                                                                    size=30
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        ft.ResponsiveRow(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Container(
                                                    expand=True,
                                                    gradient=ft.LinearGradient(
                                                        colors=[
                                                            "",
                                                            ""
                                                        ],
                                                        begin=ft.alignment.top_left,
                                                        end=ft.alignment.top_right
                                                    ),
                                                    content=ft.Column(
                                                        controls=[

                                                        ]
                                                    ),
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
                                    ]
                                )
                            )
                        )
                    ]
                )
            ]
        )
