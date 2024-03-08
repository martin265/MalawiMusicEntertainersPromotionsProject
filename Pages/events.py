import flet as ft


class InputControls(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  ============ the input controls will be here ========= //
        self.page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }
        #  =========== the input fields here ========== //


class EventsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  ======== the fonts for the system will be here ======= //
        self.page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }

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
                                        margin=ft.margin.only(top=40),
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Icon(
                                                            ft.icons.EVENT_NOTE_ROUNDED,
                                                            size=60,
                                                            color="#212121"
                                                        )
                                                    ]
                                                ),
                                                # ====== container for the text ======== //
                                                ft.Container(
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Text(
                                                                "add event details".title(),
                                                                size=30,
                                                                style=ft.TextStyle(
                                                                    font_family="manrop-bold"
                                                                )
                                                            )
                                                        ]
                                                    )
                                                ),

                                                #  ========= container for some additional cards ======= //
                                                ft.Container(
                                                    content=ft.SafeArea(
                                                        content=ft.ResponsiveRow(
                                                            [
                                                                #  ======== the text fields will be here

                                                            ]
                                                        )
                                                    )
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