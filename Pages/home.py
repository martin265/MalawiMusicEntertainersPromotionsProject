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
                                margin=ft.margin.only(bottom=40),
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
                                                            "#0075BD",
                                                            "#0099C4"
                                                        ],
                                                        begin=ft.alignment.top_left,
                                                        end=ft.alignment.top_right
                                                    ),
                                                    border_radius=ft.border_radius.all(8),
                                                    content=ft.Column(
                                                        controls=[
                                                            #  ============ // container for the events // ======//
                                                            ft.Container(
                                                                margin=ft.margin.only(top=20),
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Icon(
                                                                            ft.icons.MY_LIBRARY_MUSIC_ROUNDED,
                                                                            color="#f5f5f5",
                                                                            size=60
                                                                        ),
                                                                    ]
                                                                )
                                                            ),

                                                            #  ============ // container for the events // ======//
                                                            ft.Container(
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Text(
                                                                            "artists".capitalize(),
                                                                            font_family="manrope-sem-bold",
                                                                            size=30,
                                                                            color="#f5f5f5"
                                                                        )
                                                                    ]
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                    col={"sm": 11.5, "md": 11.5, "lg": 3.8}
                                                ),
                                                ft.Container(
                                                    expand=True,
                                                    gradient=ft.LinearGradient(
                                                        colors=[
                                                            "#00583B",
                                                            "#008D6A"
                                                        ],
                                                        begin=ft.alignment.top_left,
                                                        end=ft.alignment.top_right
                                                    ),
                                                    border_radius=ft.border_radius.all(8),
                                                    content=ft.Column(
                                                        controls=[
                                                            #  ============ // container for the events // ======//
                                                            ft.Container(
                                                                margin=ft.margin.only(top=20),
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Icon(
                                                                            ft.icons.PAYMENTS_ROUNDED,
                                                                            color="#f5f5f5",
                                                                            size=60
                                                                        ),
                                                                    ]
                                                                )
                                                            ),

                                                            #  ============ // container for the events // ======//
                                                            ft.Container(
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Text(
                                                                            "payments".capitalize(),
                                                                            font_family="manrope-sem-bold",
                                                                            size=30,
                                                                            color="#f5f5f5"
                                                                        )
                                                                    ]
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                    col={"sm": 11.5, "md": 11.5, "lg": 3.8}
                                                ),

                                                ft.Container(
                                                    expand=True,
                                                    gradient=ft.LinearGradient(
                                                        colors=[
                                                            "#69BAA4",
                                                            "#4F8073"
                                                        ],
                                                        begin=ft.alignment.top_left,
                                                        end=ft.alignment.top_right
                                                    ),
                                                    border_radius=ft.border_radius.all(8),
                                                    content=ft.Column(
                                                        controls=[
                                                            #  ============ // container for the events // ======//
                                                            ft.Container(
                                                                margin=ft.margin.only(top=20),
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Icon(
                                                                            ft.icons.EVENT_NOTE_ROUNDED,
                                                                            color="#f5f5f5",
                                                                            size=60
                                                                        ),
                                                                    ]
                                                                )
                                                            ),

                                                            #  ============ // container for the events // ======//
                                                            ft.Container(
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Text(
                                                                            "events".capitalize(),
                                                                            font_family="manrope-sem-bold",
                                                                            size=30,
                                                                            color="#f5f5f5"
                                                                        )
                                                                    ]
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                    col={"sm": 11.5, "md": 11.5, "lg": 3.8}
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
