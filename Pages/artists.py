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

        # ================= // ====================== //
        self.email = ft.TextField(
            prefix_icon=ft.icons.EMAIL_ROUNDED,
            helper_text="enter valid email".title(),
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
            label="email".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
        )

        #  =========== the input controls will be here ======= //
        self.phone_number = ft.TextField(
            prefix_icon=ft.icons.PHONE_IPHONE_ROUNDED,
            helper_text="phone number".title(),
            helper_style=ft.TextStyle(
                color="#212121",
                size=10,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            keyboard_type=ft.KeyboardType.NUMBER,
            border_radius=ft.border_radius.all(5),
            border_color="#212121",
            text_size=14,
            text_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            label="phone number".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
        )

        #  ========== for the age and gender here =============== //
        self.gender = ft.Dropdown(
            prefix_icon=ft.icons.TRANSGENDER_ROUNDED,
            helper_text="select your gender".title(),
            helper_style=ft.TextStyle(
                color="#212121",
                size=10,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            border_radius=ft.border_radius.all(5),
            border_color="#212121",
            text_size=14,
            text_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            label="gender".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
            options=[
                ft.dropdown.Option("Male"),
                ft.dropdown.Option("Female")
            ]
        )

        # ======================= the input for the age here ============== //
        self.age = ft.TextField(
            prefix_icon=ft.icons.NUMBERS_ROUNDED,
            helper_text="enter your age".title(),
            helper_style=ft.TextStyle(
                color="#212121",
                size=10,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            keyboard_type=ft.KeyboardType.NUMBER,
            border_radius=ft.border_radius.all(5),
            border_color="#212121",
            text_size=14,
            text_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            label="age".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
        )

        #  ========== for the age and gender here =============== //
        self.genre = ft.Dropdown(
            prefix_icon=ft.icons.RECORD_VOICE_OVER_ROUNDED,
            helper_text="select artist genre".title(),
            helper_style=ft.TextStyle(
                color="#212121",
                size=10,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            border_radius=ft.border_radius.all(5),
            border_color="#212121",
            text_size=14,
            text_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            label="genre".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
            options=[
                ft.dropdown.Option("Hip Hop"),
                ft.dropdown.Option("Local"),
                ft.dropdown.Option("Dance hall"),
                ft.dropdown.Option("RNb"),
            ]
        )

        # ======================= the input for the age here ============== //
        self.residence = ft.TextField(
            prefix_icon=ft.icons.LOCATION_ON_ROUNDED,
            helper_text="enter artist location".title(),
            helper_style=ft.TextStyle(
                color="#212121",
                size=10,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            keyboard_type=ft.KeyboardType.NUMBER,
            border_radius=ft.border_radius.all(5),
            border_color="#212121",
            text_size=14,
            text_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            label="artist location".title(),
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
                                                            col={"sm": 5.5, "md": 5.5, "lg": 5.5}
                                                        ),
                                                        ft.Container(
                                                            content=self.inputControls.last_name,
                                                            col={"sm": 5.5, "md": 5.5, "lg": 5.5}
                                                        ),
                                                    ]
                                                ),
                                                # ============= the other row will be here ============ //
                                                ft.ResponsiveRow(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Container(
                                                            content=self.inputControls.email,
                                                            col={"sm": 5.5, "md": 5.5, "lg": 5.5}
                                                        ),
                                                        ft.Container(
                                                            content=self.inputControls.phone_number,
                                                            col={"sm": 5.5, "md": 5.5, "lg": 5.5}
                                                        ),
                                                    ]
                                                ),
                                                # ============= the other row will be here ============ //
                                                ft.ResponsiveRow(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Container(
                                                            content=self.inputControls.age,
                                                            col={"sm": 5.5, "md": 5.5, "lg": 5.5}
                                                        ),
                                                        ft.Container(
                                                            content=self.inputControls.gender,
                                                            col={"sm": 5.5, "md": 5.5, "lg": 5.5}
                                                        ),
                                                    ]
                                                ),

                                                # ============= the other row will be here ============ //
                                                ft.ResponsiveRow(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Container(
                                                            content=self.inputControls.genre,
                                                            col={"sm": 5.5, "md": 5.5, "lg": 5.5}
                                                        ),
                                                        ft.Container(
                                                            content=self.inputControls.residence,
                                                            col={"sm": 5.5, "md": 5.5, "lg": 5.5}
                                                        ),
                                                    ]
                                                ),

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
