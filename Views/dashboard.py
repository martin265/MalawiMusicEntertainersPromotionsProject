import flet as ft
# getting the pages here
from Pages.events import EventsPage
from Pages.artists import Artists
from Pages.records import Records
from Pages.home import Home


class Dashboard(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/dashboard")
        self.page = page
        self.page.theme_mode = "light"
        #  ======== the fonts for the system will be here ======= //
        self.page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }

        # =============== list for all the pages will be here ===//
        self.all_available_pages = [
            Home(page=page),
            
            Artists(page=page),
            Records(page=page)
        ]
        #  the navigation for the system will be here ==== //
        self.navigation_rail = ft.NavigationRail(
            leading=ft.FloatingActionButton(
                content=ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(
                                ft.icons.MUSIC_NOTE_ROUNDED,
                                size=30
                            )
                        ]
                    )
                )
            ),
            selected_index=1,
            group_alignment=-0.9,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=80,
            min_extended_width=250,
            extended=False,

            #  ============ the destinations for the page will be here ======= //
            destinations=[
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.DASHBOARD_ROUNDED,
                        size=30,
                        color="#212121",
                        tooltip="home".title(),
                    ),
                    label_content=ft.Text(
                        "home".title(),
                        style=ft.TextStyle(
                            size=15,
                            font_family="manrop-bold"
                        ),
                        tooltip="home".title()
                    )
                ),

                # =============== // destination for the artists page ============ //
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.MIC_ROUNDED,
                        size=30,
                        color="#212121",
                        tooltip="artist".title(),
                    ),
                    label_content=ft.Text(
                        "artist".title(),
                        style=ft.TextStyle(
                            size=15,
                            font_family="manrop-bold"
                        ),
                        tooltip="artist".title()
                    ),
                    selected_icon_content=ft.Icon(
                        ft.icons.MIC_EXTERNAL_ON_ROUNDED,
                        size=30,
                        color="#212121",
                        tooltip="artist".title(),
                    ),
                ),

                # =============== // destination for the artists page ============ //
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.AIRPLANE_TICKET_OUTLINED,
                        size=30,
                        color="#212121",
                        tooltip="tickets".title(),
                    ),
                    label_content=ft.Text(
                        "tickets".title(),
                        style=ft.TextStyle(
                            size=15,
                            font_family="manrop-bold"
                        ),
                        tooltip="tickets".title()
                    ),
                    selected_icon_content=ft.Icon(
                        ft.icons.AIRPLANE_TICKET_ROUNDED,
                        size=30,
                        color="#212121",
                        tooltip="artist".title(),
                    ),
                ),

                # =============== // destination for the artists page ============ //
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.FILE_COPY_OUTLINED,
                        size=30,
                        color="#212121",
                        tooltip="events".title(),
                    ),
                    label_content=ft.Text(
                        "records".title(),
                        style=ft.TextStyle(
                            size=15,
                            font_family="manrop-bold"
                        ),
                        tooltip="records".title()
                    ),
                    selected_icon_content=ft.Icon(
                        ft.icons.FILE_COPY_ROUNDED,
                        size=30,
                        color="#212121",
                        tooltip="artist".title(),
                    ),
                ),
            ],
            on_change=self.destination_page
        )
        #  ============ calling the function here ======== //
        self.selected_page_transitions()

        #  ========== returning the controls here
        self.controls = [
            ft.Row(
                controls=[
                    self.navigation_rail,
                    ft.Column(self.all_available_pages, alignment=ft.MainAxisAlignment.START, expand=True),
                ],
                expand=True
            )
        ]

    #  ========== functions to control page transitions
    def selected_page_transitions(self):
        try:
            for index, single_page in enumerate(self.all_available_pages):
                single_page.visible = True if index == self.navigation_rail.selected_index else False
                self.update()
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

    #  ======== function to get the selected page here ========== //
    def destination_page(self, e):
        try:
            self.selected_page_transitions()
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
