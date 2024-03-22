import flet as ft


class Tickets(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }
        #  ========= the content for the tickets page will be here ==== //
        self.content = ft.Column(
            controls=[
                ft.SafeArea(
                    content=ft.ResponsiveRow(
                        controls=[
                            #  ========== the container for the form here
                            ft.Container(
                                expand=True,
                                gradient=ft.LinearGradient(
                                    colors=[
                                        "#272729",
                                        "#212121"
                                    ],
                                    begin=ft.alignment.top_left,
                                    end=ft.alignment.bottom_right
                                ),
                                border_radius=ft.border_radius.all(8),
                                content=ft.Column(
                                    controls=[
                                        #  =========== the container for the top text
                                        ft.Container(
                                            margin=ft.margin.only(top=30),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        "add tickets details".capitalize(),
                                                        color="white",
                                                        size=30,
                                                        font_family="manrop-bold"
                                                    )
                                                ]
                                            )
                                        ),

                                        # ========== the container for the icon =========== //
                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.AIRPLANE_TICKET_ROUNDED,
                                                        size=50,
                                                        color="#00C896"
                                                    )
                                                ]
                                            )
                                        ),


                                        # ============ the container for the input controls ======= //


                                    ]
                                ),
                                col={"sm": 12, "md": 8, "lg": 8}
                            ),
                            #  =========== the container for the other tools
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            "hello"
                                        )
                                    ]
                                ),
                                col={"sm": 12, "md": 4, "lg": 4}
                            )
                        ]
                    )
                )
            ]
        )