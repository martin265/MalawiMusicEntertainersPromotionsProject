import flet as ft


class TicketControls(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        # ============ // ============== //
        self.ticket_type = ft.TextField(
            hint_text="select ticket type",
            helper_text="select ticket type",
            keyboard_type=ft.KeyboardType.TEXT,
            label="ticket type"
        )

        # ================= // ======================= //
        self.ticket_price = ft.TextField(
            hint_text="select ticket price",
            helper_text="select ticket price",
            keyboard_type=ft.KeyboardType.TEXT,
            label="ticket price"
        )

        # ================= // ======================= //
        self.event_name = ft.TextField(
            helper_text="enter event name".capitalize(),
            keyboard_type=ft.KeyboardType.TEXT,
            label="events name"
        )

        # ================= // ======================= //
        self.event_type = ft.TextField(
            helper_text="enter event type".capitalize(),
            keyboard_type=ft.KeyboardType.TEXT,
            label="events type"
        )

        # ================= // ======================= //
        self.event_capacity = ft.TextField(
            helper_text="allowable capacity".capitalize(),
            keyboard_type=ft.KeyboardType.TEXT,
            label="event capacity"
        )

        # ================= // ======================= //
        self.event_organizers = ft.TextField(
            helper_text="enter event organizers".capitalize(),
            keyboard_type=ft.KeyboardType.TEXT,
            label="events organizers"
        )

        # ================= // ======================= //
        self.special_offers = ft.Dropdown(
            helper_text="special offers".capitalize(),
            label="special offers",
            options=[
                ft.dropdown.Option("Early Bird Discount"),
                ft.dropdown.Option("Group Discounts"),
                ft.dropdown.Option("Bundle Deals"),
                ft.dropdown.Option("Student or Senior Discounts"),
                ft.dropdown.Option("Flash Sales"),
                ft.dropdown.Option("Holiday or Seasonal Promotions"),
                ft.dropdown.Option("Exclusive Access Events"),
            ]
        )

        # ================= // ======================= //
        self.accessibility_information = ft.TextField(
            helper_text="enter accessibility information".capitalize(),
            keyboard_type=ft.KeyboardType.TEXT,
            label="accessibility information"
        )

        # ================= // ======================= //
        self.age_restrictions = ft.TextField(
            helper_text="enter the restricted age".capitalize(),
            keyboard_type=ft.KeyboardType.NUMBER,
            label="age limits"
        )

        # ================= // ======================= //
        self.event_description = ft.TextField(
            helper_text="enter event description".capitalize(),
            keyboard_type=ft.KeyboardType.TEXT,
            label="event description"
        )

        # ================= // ======================= //
        self.payment_method = ft.Dropdown(
            helper_text="select payment method".capitalize(),
            label="payment method",
            options=[
                ft.dropdown.Option("Cash"),
                ft.dropdown.Option("VISA Card"),
                ft.dropdown.Option("Mpamba"),
                ft.dropdown.Option("Airtel Money"),
            ]
        )

        # ================= // ======================= //
        self.event_category = ft.Dropdown(
            helper_text="event category".capitalize(),
            label="event category",
            options=[
                ft.dropdown.Option("Conference".title()),
                ft.dropdown.Option("Concert".title()),
                ft.dropdown.Option("workshop".title()),
                ft.dropdown.Option("fundraiser".title())
            ]
        )

        # ================= // ======================= //
        self.artist_name = ft.Dropdown(
            helper_text="select artists name".capitalize(),
            label="artists name",
            options=[
                ft.dropdown.Option("Conference".title()),
            ]
        )

    def validate_event_details(self, e):
        """function will validate the input fields"""
        try:
            if not self.ticket_type.value:
                self.ticket_type.error_text = "enter the ticket type".capitalize()
                self.page.update()
            # ================= // =================== //
            elif not self.ticket_price.value:
                self.ticket_price.error_text = "enter the ticket price".capitalize()
                self.page.update()
                # ================= // =================== //
            elif not self.event_name.value:
                self.event_name.error_text = "provide the event name".capitalize()
                self.page.update()

            elif not self.event_type.value:
                self.event_type.error_text = "enter event type".capitalize()
                self.page.update()

            elif not self.event_capacity.value:
                self.event_capacity.error_text = "event capacity".capitalize()
                self.page.update()

            elif not self.event_organizers.value:
                self.event_organizers.error_text = "provide something".capitalize()
                self.page.update()

            elif not self.special_offers.value:
                self.special_offers.error_text = "provide the special offers".capitalize()
                self.page.update()

            elif not self.accessibility_information.value:
                self.accessibility_information.error_text = "enter some text"
                self.page.update()

            elif not self.age_restrictions.value:
                self.age_restrictions.error_text = "enter the age".capitalize()
                self.page.update()


            elif not self.event_description.value:
                self.event_description.error_text = "provide the description".capitalize()
                self.page.update()


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


class TicketsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.adaptive = True
        #  ======== the fonts for the system will be here ======= //
        self.page.scroll = ft.ScrollMode.ADAPTIVE
        self.page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }
        # ============ getting the input controls here ============ //
        self.inputControls = TicketControls(page=page)
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
                                                    "add event details".title(),
                                                    size=30,
                                                    font_family="manrop-bold"
                                                )
                                            ]
                                        )
                                    ),

                                    # =============== // container for the icon will be here ======== //
                                    ft.Container(
                                        margin=ft.margin.only(top=10, bottom=40),
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Icon(
                                                    ft.icons.EVENT_NOTE_ROUNDED,
                                                    size=50,
                                                    color="#212121"
                                                )
                                            ]
                                        )
                                    ),

                                    # ============== /ticket controls will be here/ ==================== //
                                    ft.ResponsiveRow(
                                        adaptive=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.ticket_type,
                                                col={"sm": 12, "md": 12, "lg": 5.5}
                                            ),

                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.ticket_price,
                                                col={"sm": 12, "md": 12, "lg": 5.5}
                                            ),

                                        ]
                                    ),
                                    # ============== /ticket controls will be here/ ==================== //
                                    ft.ResponsiveRow(
                                        adaptive=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.event_name,
                                                col={"sm": 12, "md": 12, "lg": 5.5}
                                            ),

                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.event_type,
                                                col={"sm": 12, "md": 12, "lg": 5.5}
                                            ),

                                        ]
                                    ),
                                    # ============== /ticket controls will be here/ ==================== //
                                    ft.ResponsiveRow(
                                        adaptive=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.event_capacity,
                                                col={"sm": 12, "md": 12, "lg": 5.5}
                                            ),

                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.event_organizers,
                                                col={"sm": 12, "md": 12, "lg": 5.5}
                                            ),

                                        ]
                                    ),
                                    # ============== /ticket controls will be here/ ==================== //
                                    ft.ResponsiveRow(
                                        adaptive=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.special_offers,
                                                col={"sm": 11.5, "md": 11.5, "lg": 5.5}
                                            ),

                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.accessibility_information,
                                                col={"sm": 11.5, "md": 11.5, "lg": 5.5}
                                            ),

                                        ]
                                    ),

                                    ft.ResponsiveRow(
                                        adaptive=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.age_restrictions,
                                                col={"sm": 11.5, "md": 11.5, "lg": 5.5}
                                            ),

                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.event_description,
                                                col={"sm": 11.5, "md": 11.5, "lg": 5.5}
                                            ),

                                        ]
                                    ),

                                    ft.ResponsiveRow(
                                        adaptive=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.payment_method,
                                                col={"sm": 11.5, "md": 11.5, "lg": 5.5}
                                            ),

                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.event_category,
                                                col={"sm": 11.5, "md": 11.5, "lg": 5.5}
                                            ),

                                        ]
                                    ),

                                    ft.ResponsiveRow(
                                        adaptive=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.artist_name,
                                                col={"sm": 11.5, "md": 11.5, "lg": 11}
                                            ),
                                        ]
                                    )

                                ]
                            ),
                            col={"sm": 12, "md": 12, "lg": 12}
                        )
                    ]
                )
            ]
        )
