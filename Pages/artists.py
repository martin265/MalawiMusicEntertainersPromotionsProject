import flet as ft


class InputControls(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }
        #  =========== the input controls will be here ======= //
        self.first_name = ft.TextField(
            prefix_icon=ft.icons.EDIT_DOCUMENT,
            helper_text="enter first name".title(),
            helper_style=ft.TextStyle(
                color="#212121",
                size=10,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            keyboard_type=ft.KeyboardType.TEXT,
            border_radius=ft.border_radius.all(5),
            border_color="#212121",
            text_size=14,
            text_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            label="first name".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
        )

        #  =========== the input controls will be here ======= //
        self.last_name = ft.TextField(
            prefix_icon=ft.icons.EDIT_DOCUMENT,
            helper_text="last name".title(),
            helper_style=ft.TextStyle(
                color="#212121",
                size=10,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            keyboard_type=ft.KeyboardType.TEXT,
            border_radius=ft.border_radius.all(5),
            border_color="#212121",
            text_size=14,
            text_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            label="last name".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
        )


class Artists(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  ======== passing the input fields ============ //
        self.inputControls = InputControls(page=page)
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
                            bgcolor=ft.colors.BLACK,
                            border_radius=ft.border_radius.all(10),
                            gradient=ft.LinearGradient(
                                colors=[
                                    "#CBCCFF",
                                    "#CBCCFF"
                                ],
                                begin=ft.alignment.top_right,
                                end=ft.alignment.bottom_left,
                            ),
                            content=ft.Column(
                                controls=[
                                    #  ========== the top container for the controls will be here ======= //
                                    ft.Container(
                                        margin=ft.margin.only(top=40),
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text(
                                                    "add artist details".title(),
                                                    font_family="manrop-bold",
                                                    style=ft.TextStyle(
                                                        color="#212121"
                                                    ),
                                                    size=30
                                                )
                                            ]
                                        )
                                    ),

                                    #  ============= container for the icon will be here ========= //
                                    ft.Container(
                                        margin=ft.margin.only(top=20),
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Icon(
                                                    ft.icons.MIC_ROUNDED,
                                                    size=70,
                                                    color="#212121"
                                                )
                                            ]
                                        )
                                    ),

                                    # ============= container for the input fields will be here ======= //
                                    ft.Container(
                                        margin=ft.margin.only(top=30),
                                        content=ft.Column(
                                            controls=[
                                                ft.ResponsiveRow(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Container(
                                                            content=self.inputControls.first_name,
                                                            col={"sm": 12, "md": 6, "lg": 5.5}
                                                        ),
                                                        ft.Container(
                                                            content=self.inputControls.first_name,
                                                            col={"sm": 12, "md": 6, "lg": 5.5}
                                                        ),
                                                    ]
                                                )
                                            ]
                                        )
                                    )
                                ]
                            ),
                            col={"sm": 12, "md": 12, "lg": 9}
                        )
                    ]
                )
            ]
        )
