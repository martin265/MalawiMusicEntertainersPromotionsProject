import flet as ft


class TicketControls(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        # ============ // ============== //
        self.ticket_type = ft.TextField(
            hint_text="select ticket type",
            helper_text="select ticket type"
        )

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
                                        margin=ft.margin.only(top=30),
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text(
                                                    "add ticket details".title(),
                                                    size=30,
                                                    font_family="manrop-bold"
                                                )
                                            ]
                                        )
                                    ),

                                    # =============== // container for the icon will be here ======== //
                                    ft.Container(
                                        margin=ft.margin.only(top=10),
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Icon(
                                                    ft.icons.AIRPLANE_TICKET_ROUNDED,
                                                    size=50,
                                                    color="#212121"
                                                )
                                            ]
                                        )
                                    ),

                                    # ============== /ticket controls will be here/ ==================== //
                                ]
                            ),
                            col={"sm": 12, "md": 12, "lg": 12}
                        )
                    ]
                )
            ]
        )
