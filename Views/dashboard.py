import flet as ft


class Dashboard(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/dashboard")
        self.page = page
        #  ======== the fonts for the system will be here ======= //
        page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }
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
            selected_index=0,
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
                            size=18,
                            font_family="manrop-bold"
                        ),
                        tooltip="home".title()
                    )
                ),

                # ============ // the other navigation component will be here ===== //
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.EVENT_NOTE_ROUNDED,
                        size=30,
                        color="#212121",
                        tooltip="events".title(),
                    ),
                    label_content=ft.Text(
                        "home".title(),
                        style=ft.TextStyle(
                            size=18,
                            font_family="manrop-bold"
                        ),
                        tooltip="events".title()
                    )
                ),
            ]
        )
        #  ========== returning the controls here
        self.controls = [
            ft.SafeArea(
                content=ft.Container(
                    content=ft.Text(
                        "hello",
                        color="black"
                    )
                )
            )
        ]
