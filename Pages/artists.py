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
        self.selected_files = ft.Text()
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
            keyboard_type=ft.KeyboardType.EMAIL,
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

        #  ============== the artists bio will be here =========== //
        self.artist_biography = ft.TextField(
            prefix_icon=ft.icons.INFO_OUTLINE_ROUNDED,
            helper_text="enter artist bio".title(),
            helper_style=ft.TextStyle(
                color="#212121",
                size=10,
                font_family="manrope-sem-bold",
                weight=ft.FontWeight.BOLD
            ),
            multiline=True,
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
            label="artist bio".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
        )

        #  ============ button to save the records here =============== //
        self.save_records_button = ft.ElevatedButton(
            adaptive=True,
            bgcolor="#212121",
            icon=ft.icons.SAVE_ROUNDED,
            text="save artist records",
            color="white",
            height=50,
            style=ft.ButtonStyle(
                elevation=None,
                shadow_color="#7F4D3E",
            ),
            on_click=self.validate_artist_records
        )

    #  =========== function to validate the records here =========== //
    def validate_artist_records(self, e):
        """the function will be used in validating the input fields"""
        try:
            if not self.first_name.value:
                self.first_name.error_text = "fill in the blanks".capitalize()
                self.first_name.error_style = ft.TextStyle(
                    color="#d50000",
                    size=15,
                    font_family="manrope-sem-bold",
                )
                self.page.update()
            #  =============== // ================== //
            elif not self.last_name.value:
                self.last_name.error_text = "enter the last name ".capitalize()
                self.last_name.error_style = ft.TextStyle(
                    color="#d50000",
                    size=15,
                    font_family="manrope-sem-bold",
                )
                self.page.update()

            # ===================== // ================= //
            elif not self.email.value:
                self.email.error_text = "provide an email".capitalize()
                self.email.error_style = ft.TextStyle(
                    color="#d50000",
                    size=15,
                    font_family="manrope-sem-bold",
                )
                self.page.update()
            # ===================== // ===================== //
            elif not self.phone_number.value:
                self.phone_number.error_text = "fill something for the phone number".capitalize()
                self.phone_number.error_style = ft.TextStyle(
                    color="#d50000",
                    size=15,
                    font_family="manrope-sem-bold",
                )
                self.page.update()
            #  =================== // ==================== //
            elif not self.gender.value:
                self.gender.error_text = "select your gender first".capitalize()
                self.gender.error_style = ft.TextStyle(
                    color="#d50000",
                    size=15,
                    font_family="manrope-sem-bold",
                )
                self.page.update()
            #  =================== // ======================== //
            elif not self.age.value:
                self.age.error_text = "pass in your age please".capitalize()
                self.age.error_style = ft.TextStyle(
                    color="#d50000",
                    size=15,
                    font_family="manrope-sem-bold",
                )
                self.page.update()
            #  ==================== // ========================== //
            elif not self.genre.value:
                self.genre.error_text = "select the genre first".capitalize()
                self.genre.error_style = ft.TextStyle(
                    color="#d50000",
                    size=15,
                    font_family="manrope-sem-bold",
                )
                self.page.update()
            #  ======================== // ===================== //
            elif not self.residence.value:
                self.residence.error_text = "enter the artists location".capitalize()
                self.residence.error_style = ft.TextStyle(
                    color="#d50000",
                    size=15,
                    font_family="manrope-sem-bold",
                )
                self.page.update()
            #  ================= // the input for the artist biography will be here ======== //
            elif not self.artist_biography.value:
                self.artist_biography.error_text = "enter the artist biography".capitalize()
                self.residence.error_style = ft.TextStyle(
                    color="#d50000",
                    size=15,
                    font_family="manrope-sem-bold",
                )
                self.page.update()
            else:

                print(self.message)
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()


    def upload_profile_picture(self, e:ft.FilePickerUploadEvent):
        self.selected_files.value = (

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
            height=self.page.height,
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

                                                #  ============ adding the button to save the artists records here == //
                                                ft.ResponsiveRow(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Container(
                                                            content=self.inputControls.artist_biography,
                                                            col={"sm": 5.5, "md": 5.5, "lg": 11}
                                                        ),
                                                    ]
                                                ),

                                                #  ============ adding the button to save the artists records here == //
                                                ft.ResponsiveRow(
                                                    alignment=ft.MainAxisAlignment.START,
                                                    controls=[
                                                        ft.Container(
                                                            margin=ft.margin.only(left=30, bottom=20, top=20),
                                                            content=self.inputControls.save_records_button,
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
                        ),

                        #  ============ the side container for the page =============== //
                        ft.Container(
                            expand=True,
                            bgcolor=ft.colors.BLACK,
                            border_radius=ft.border_radius.all(10),
                            height=400,
                            margin=ft.margin.only(bottom=30),
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
                                    ft.Image(
                                        width=self.page.width,
                                        src="https://images.pexels.com/photos/755416/pexels-photo-755416.jpeg?auto"
                                            "=compress&cs=tinysrgb&w=600",
                                        border_radius=ft.border_radius.only(top_left=10, top_right=10),
                                        col={"sm": 12, "md": 12, "lg": 3}
                                    ),

                                    ft.Text(
                                        f"the message is {self.inputControls.first_name.value}"
                                    )
                                ]
                            ),
                            col={"sm": 12, "md": 12, "lg": 3}
                        )

                    ]
                ),

            ]
        )
