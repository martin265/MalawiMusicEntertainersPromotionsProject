import flet as ft


class Artists(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  ======== the fonts for the system will be here ======= //
        self.page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }
        # =========== the content for the main dashboard will be here ======== //
        self.content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            adaptive=True,
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            expand=True,
                            content=ft.Text("hello"),
                            bgcolor=ft.colors.BLACK,
                            border_radius=ft.border_radius.all(10),
                            gradient=ft.LinearGradient(
                                colors=[
                                    "",
                                    ""
                                ],
                                begin=ft.alignment.top_right,
                                end=ft.alignment.bottom_left,
                            ),
                            col={"sm": 12, "md": 12, "lg": 9}
                        )
                    ]
                )
            ]
        )