import flet as ft


class TicketsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.adaptive = True
        #  ======== the fonts for the system will be here ======= //
        self.page.scroll = ft.ScrollMode.HIDDEN
        self.page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }
        # =============== // adding the controls to the page here ========== //
        self.content = ft.Column(
            height=self.page.height,
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            gradient=ft.LinearGradient(
                                colors=[
                                    "#CBCCFF",
                                    "#CBCCFF"
                                ],
                                begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_center
                            ),
                            border_radius=ft.border_radius.all(10),
                            content=ft.Column(
                                controls=[
                                    # ============ // container for the top text // ======
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                ft.Text(
                                                    "add ticket details".title(),
                                                    size=30,
                                                    font_family="manrop-bold"
                                                )
                                            ]
                                        )
                                    )
                                ]
                            ),
                            col={"sm": 12, "md": 12, "lg": 12}
                        )
                    ]
                )
            ]
        )
