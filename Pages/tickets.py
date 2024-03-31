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
            label="events name"
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
        self.age_restrictions = ft.Dropdown(
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
                                                    "add ticket details".title(),
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
                                                    ft.icons.AIRPLANE_TICKET_ROUNDED,
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
                                                content=self.inputControls.ticket_type,
                                                col={"sm": 12, "md": 12, "lg": 5.5}
                                            ),

                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.ticket_type,
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
                                                content=self.inputControls.ticket_type,
                                                col={"sm": 12, "md": 12, "lg": 5.5}
                                            ),

                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.ticket_type,
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
                                                content=self.inputControls.ticket_type,
                                                col={"sm": 11.5, "md": 11.5, "lg": 5.5}
                                            ),

                                            ft.Container(
                                                expand=True,
                                                content=self.inputControls.ticket_type,
                                                col={"sm": 11.5, "md": 11.5, "lg": 5.5}
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
