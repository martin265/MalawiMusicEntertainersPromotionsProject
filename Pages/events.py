import flet as ft
import datetime


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
        self.event_title = ft.TextField(
            prefix_icon=ft.icons.TITLE_ROUNDED,
            helper_text="enter event title".title(),
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
            label="event title".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
        )

        self.event_description = ft.TextField(
            prefix_icon=ft.icons.DESCRIPTION_ROUNDED,
            helper_text="enter event description".title(),
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
            label="event description".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
        )

        #  ============== drop down for the event category
        self.event_category = ft.Dropdown(
            prefix_icon=ft.icons.CATEGORY_ROUNDED,
            helper_text="select event category".title(),
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
            label="event category".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
            options=[
                ft.dropdown.Option("Conference".title()),
                ft.dropdown.Option("Concert".title()),
                ft.dropdown.Option("workshop".title()),
                ft.dropdown.Option("fundraiser".title())
            ]
        )

        #  ============== drop down for the event category
        self.event_location = ft.Dropdown(
            prefix_icon=ft.icons.LOCATION_ON_ROUNDED,
            prefix_style=ft.TextStyle(
                color="blue"
            ),
            helper_text="select event location".title(),
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
            label="event location".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
            options=[
                ft.dropdown.Option("Lilongwe"),
                ft.dropdown.Option("Blantyre"),
                ft.dropdown.Option("Zomba"),
                ft.dropdown.Option("Mzuzu"),
                ft.dropdown.Option("Karonga"),
                ft.dropdown.Option("Mulanje"),
            ]
        )

        #  ============== the fields for the event date and the event time ============ //
        self.event_date = ft.DatePicker(
            first_date=datetime.datetime(2021, 1, 1, 1),
            last_date=datetime.datetime(2030, 1, 1, 1),
        )
        self.page.overlay.append(self.event_date)
        #  ========== the button to select the date here ======== //
        self.event_start_button = ft.ElevatedButton(
            text="select event start date".title(),
            icon=ft.icons.DATE_RANGE_ROUNDED,
            icon_color="#f5f5f5",
            bgcolor="#212121",
            color="#f5f5f5",
            height=50,
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: "#212121",
                },
            ),
            on_click=lambda _: self.event_date.pick_date()
        )

        #  ============ event end date will be here =============== //
        self.event_end_date = ft.DatePicker(
            first_date=datetime.datetime(2021, 1, 1, 1),
            last_date=datetime.datetime(2030, 1, 1, 1),
        )
        self.page.overlay.append(self.event_end_date)
        #  ========== the button to select the date here ======== //
        self.event_end_button = ft.ElevatedButton(
            text="select event end date".title(),
            icon=ft.icons.CALENDAR_VIEW_DAY_ROUNDED,
            icon_color="#f5f5f5",
            bgcolor="#412728",
            color="#f5f5f5",
            height=50,
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: "#212121"
                },
            ),
            on_click=lambda _: self.event_end_date.pick_date()
        )

        #  ============ event end date will be here =============== //
        self.event_time = ft.TimePicker(
            confirm_text="Confirm",
            error_invalid_text="Time out of range",
            help_text="Pick your time slot",
        )
        self.page.overlay.append(self.event_time)
        #  ========== the button to select the date here ======== //
        self.event_time_button = ft.ElevatedButton(
            text="select event end date".title(),
            icon=ft.icons.TIMER_ROUNDED,
            icon_color="#f5f5f5",
            bgcolor="#7F4D3E",
            color="#f5f5f5",
            height=50,
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: "#212121"
                },
            ),
            on_click=lambda _: self.event_time.pick_time()
        )

        # =============== // drop down for the ticket types and capacity limit =========== //
        #  ============== drop down for the event category
        self.ticket_types = ft.Dropdown(
            prefix_icon=ft.icons.AIRPLANE_TICKET_ROUNDED,
            helper_text="select ticket type".title(),
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
            label="event ticket type".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
            options=[
                ft.dropdown.Option("Gold".title()),
                ft.dropdown.Option("Silver".title()),
                ft.dropdown.Option("Diamond".title()),
                ft.dropdown.Option("Basic".title())
            ]
        )

        # ==================== // ============================= //
        #  ============== drop down for the event category
        self.capacity_limit = ft.Dropdown(
            prefix_icon=ft.icons.REDUCE_CAPACITY_ROUNDED,
            helper_text="select the capacity to be accommodated".title(),
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
            label="event capacity".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
            options=[
                ft.dropdown.Option("Large".title()),
                ft.dropdown.Option("Medium".title()),
            ]
        )

        # ================= // the payment options and additional details ========== //
        self.payment_types = ft.Dropdown(
            prefix_icon=ft.icons.PAYMENT_ROUNDED,
            helper_text="select the payment type".title(),
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
            label="payment type".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
            options=[
                ft.dropdown.Option("Cash".title()),
                ft.dropdown.Option("Card".title()),
                ft.dropdown.Option("Airtel Money".title()),
                ft.dropdown.Option("Mpamba".title()),
            ]
        )

        #  ================ the description will be here ========== //
        self.additional_details = ft.TextField(
            prefix_icon=ft.icons.DETAILS_ROUNDED,
            helper_text="add other additional details".title(),
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
            label="additional details".title(),
            label_style=ft.TextStyle(
                color="#212121",
                size=14,
                font_family="manrope-sem-bold"
            ),
        )


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

        #  ================ getting the controls here from the class
        self.inputControls = InputControls(page=page)

        # ========= the user controls will be here ====== //
        self.content = ft.Container(
            adaptive=True,
            content=ft.SafeArea(
                content=ft.ResponsiveRow(
                    #  ======== the first container for the events details will be here ========= //
                    [
                        ft.Container(
                            content=ft.Column(
                                auto_scroll=True,
                                controls=[
                                    # ======== the container for the top information
                                    ft.Container(
                                        margin=ft.margin.only(top=40, bottom=30),
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
                                                    margin=ft.margin.only(top=30),
                                                    content=ft.SafeArea(
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        #  ======== the text fields will be here
                                                                        ft.Container(
                                                                            content=self.inputControls.event_title,
                                                                            col={"md": 5.5, "sm": 5.5, "lg": 5.5}
                                                                        ),

                                                                        ft.Container(
                                                                            content=self.inputControls.event_description,
                                                                            col={"md": 5.5, "sm": 5.5, "lg": 5.5}
                                                                        ),

                                                                    ],
                                                                    run_spacing=0
                                                                ),

                                                                # ============== the second control container =======
                                                                ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        #  ======== the text fields will be here
                                                                        ft.Container(
                                                                            content=self.inputControls.event_category,
                                                                            padding=ft.padding.only(top=10),
                                                                            col={"md": 5.5, "sm": 5.5, "lg": 5.5}
                                                                        ),

                                                                        ft.Container(
                                                                            content=self.inputControls.event_location,
                                                                            padding=ft.padding.only(top=10),
                                                                            col={"md": 5.5, "sm": 5.5, "lg": 5.5}
                                                                        ),

                                                                    ],
                                                                    run_spacing=0
                                                                ),

                                                                # ============== the second control container =======
                                                                ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        #  ======== the text fields will be here
                                                                        ft.Container(
                                                                            content=self.inputControls.event_start_button,
                                                                            padding=ft.padding.only(top=10),
                                                                            col={"md": 4, "sm": 3.5, "lg": 3.5}
                                                                        ),
                                                                        ft.Container(
                                                                            content=self.inputControls.event_end_button,
                                                                            padding=ft.padding.only(top=10),
                                                                            col={"md": 4, "sm": 3.5, "lg": 3.5}
                                                                        ),
                                                                        ft.Container(
                                                                            content=self.inputControls.event_time_button,
                                                                            padding=ft.padding.only(top=10),
                                                                            col={"md": 4, "sm": 3.5, "lg": 3.5}
                                                                        ),

                                                                    ],
                                                                    run_spacing=10
                                                                ),

                                                                # ============== the second control container =======
                                                                ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        #  ======== the text fields will be here
                                                                        ft.Container(
                                                                            content=self.inputControls.capacity_limit,
                                                                            padding=ft.padding.only(top=10),
                                                                            col={"md": 5.5, "sm": 5.5, "lg": 5.5}
                                                                        ),
                                                                        ft.Container(
                                                                            content=self.inputControls.ticket_types,
                                                                            padding=ft.padding.only(top=10),
                                                                            col={"md": 5.5, "sm": 5.5, "lg": 5.5}
                                                                        ),

                                                                    ],
                                                                    run_spacing=10
                                                                ),

                                                                # ============== the second control container =======
                                                                ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        #  ======== the text fields will be here
                                                                        ft.Container(
                                                                            content=self.inputControls.payment_types,
                                                                            padding=ft.padding.only(top=10),
                                                                            col={"md": 5.5, "sm": 5.5, "lg": 5.5}
                                                                        ),
                                                                        ft.Container(
                                                                            content=self.inputControls.additional_details,
                                                                            padding=ft.padding.only(top=10),
                                                                            col={"md": 5.5, "sm": 5.5, "lg": 5.5}
                                                                        ),

                                                                    ],
                                                                    run_spacing=10
                                                                ),
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
