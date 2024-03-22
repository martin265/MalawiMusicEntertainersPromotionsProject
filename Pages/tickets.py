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
        #  =========== adding the input fields for the system here ========= //
        self.ticket_type = ft.Dropdown(
            border_color="#212121",
            helper_text="select the ticket type".capitalize(),
            border_radius=ft.border_radius.all(5),
            prefix_icon=ft.icons.AIRPLANE_TICKET_ROUNDED,
            helper_style=ft.TextStyle(
                color="#212121",
                font_family="manrope-sem-bold"
            ),
            hint_text="select ticket type",
            hint_style=ft.TextStyle(
                color="#212121",
                font_family="manrope-sem-bold"
            ),
            options=[
                ft.dropdown.Option("VIP"),
                ft.dropdown.Option("GOLD"),
                ft.dropdown.Option("SILVER"),
                ft.dropdown.Option("DIAMOND"),
            ]
        )

        self.ticket_price = ft.TextField(
            border_color="#212121",
            helper_text="ticket price".capitalize(),
            border_radius=ft.border_radius.all(5),
            keyboard_type=ft.KeyboardType.NUMBER,
            prefix_icon=ft.icons.NUMBERS_ROUNDED,
            helper_style=ft.TextStyle(
                color="#212121",
                font_family="manrope-sem-bold"
            ),
            hint_text="enter ticket price",
            hint_style=ft.TextStyle(
                color="#212121",
                font_family="manrope-sem-bold"
            ),
        )

        self.ticket_purchase_limit = ft.TextField(
            border_color="#212121",
            helper_text="ticket purchase limit".capitalize(),
            border_radius=ft.border_radius.all(5),
            keyboard_type=ft.KeyboardType.NUMBER,
            prefix_icon=ft.icons.PRODUCTION_QUANTITY_LIMITS_ROUNDED,
            helper_style=ft.TextStyle(
                color="#212121",
                font_family="manrope-sem-bold"
            ),
            hint_text="enter ticket purchase limit",
            hint_style=ft.TextStyle(
                color="#212121",
                font_family="manrope-sem-bold"
            ),
        )

        self.payment_method = ft.Dropdown(
            border_color="#212121",
            helper_text="select payment method".capitalize(),
            border_radius=ft.border_radius.all(5),
            prefix_icon=ft.icons.SUPERVISOR_ACCOUNT_ROUNDED,
            helper_style=ft.TextStyle(
                color="#212121",
                font_family="manrope-sem-bold"
            ),
            hint_text="payment method",
            hint_style=ft.TextStyle(
                color="#212121",
                font_family="manrope-sem-bold"
            ),
            options=[
                ft.dropdown.Option("VISA"),
                ft.dropdown.Option("CASH"),
            ]
        )

        self.age_restriction = ft.TextField(
            border_color="#212121",
            helper_text="ticket age limit".capitalize(),
            border_radius=ft.border_radius.all(5),
            keyboard_type=ft.KeyboardType.NUMBER,
            prefix_icon=ft.icons.BLOCK_ROUNDED,
            helper_style=ft.TextStyle(
                color="#212121",
                font_family="manrope-sem-bold"
            ),
            hint_text="enter age ticket age limit",
            hint_style=ft.TextStyle(
                color="#212121",
                font_family="manrope-sem-bold"
            ),
        )

        self.ticket_available = ft.Checkbox(
            tristate=True,
            label="Available Ticket".title(),
            adaptive=True,
            label_style=ft.TextStyle(
                color="black",
                font_family="manrope-sem-bold",
                size=18
            ),
        )

        self.ticket_unavailable = ft.Checkbox(
            tristate=True,
            label="Unavailable Ticket".title(),
            label_style=ft.TextStyle(
                color="black",
                font_family="manrope-sem-bold",
                size=18
            ),
            adaptive=True,
            height=40
        )

        #  =================== // the date and time buttons for the event will be here ===== //
        self.ticket_sale_start_date = ft.OutlinedButton(
            text="select start date",
            icon=ft.icons.DATE_RANGE_ROUNDED,
            on_click={}
        )
        #  =================== // the date and time buttons for the event will be here ===== //
        self.ticket_sale_end_date = ft.OutlinedButton(
            text="select end date",
            icon=ft.icons.TIMER_ROUNDED,
            on_click={}
        )



class Tickets(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }

        # ================ getting the inputs from the other class here ============= //
        self.inputControls = InputControls(page=page)
        #  ========= the content for the tickets page will be here ==== //
        self.content = ft.Column(
            adaptive=True,
            controls=[
                ft.SafeArea(
                    adaptive=True,
                    content=ft.ResponsiveRow(
                        controls=[
                            #  ========== the container for the form here
                            ft.Container(
                                expand=True,
                                gradient=ft.LinearGradient(
                                    colors=[
                                        "#CBCCFF",
                                        "#CBCCFF"
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
                                                        color="#212121",
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
                                                        color="#292F57"
                                                    )
                                                ]
                                            )
                                        ),

                                        # ============ the container for the input controls ======= //
                                        ft.Container(
                                            margin=ft.margin.only(top=20),
                                            adaptive=True,
                                            content=ft.SafeArea(
                                                content=ft.Column(
                                                    controls=[
                                                        ft.ResponsiveRow(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Container(
                                                                    expand=True,
                                                                    content=self.inputControls.ticket_type,
                                                                    col={"sm": 12, "md": 4, "lg": 5.5}
                                                                ),
                                                                ft.Container(
                                                                    expand=True,
                                                                    content=self.inputControls.ticket_price,
                                                                    col={"sm": 12, "md": 4, "lg": 5.5}
                                                                ),
                                                            ],
                                                            run_spacing=0
                                                        ),

                                                        ft.ResponsiveRow(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Container(
                                                                    expand=True,
                                                                    content=self.inputControls.ticket_purchase_limit,
                                                                    col={"sm": 12, "md": 4, "lg": 5.5}
                                                                ),
                                                                ft.Container(
                                                                    expand=True,
                                                                    content=self.inputControls.age_restriction,
                                                                    col={"sm": 12, "md": 4, "lg": 5.5}
                                                                ),
                                                            ],
                                                            run_spacing=0
                                                        ),

                                                        ft.ResponsiveRow(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Container(
                                                                    expand=True,
                                                                    content=ft.Row(
                                                                        controls=[
                                                                            self.inputControls.ticket_available,
                                                                            self.inputControls.ticket_unavailable,
                                                                        ]
                                                                    ),
                                                                    col={"sm": 12, "md": 4, "lg": 5.5}
                                                                ),
                                                                ft.Container(
                                                                    expand=True,
                                                                    content=self.inputControls.payment_method,
                                                                    col={"sm": 12, "md": 4, "lg": 5.5}
                                                                ),
                                                            ],
                                                            run_spacing=0
                                                        )
                                                    ]
                                                )
                                            )
                                        )

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
                        ],
                        run_spacing=10
                    )
                )
            ]
        )
