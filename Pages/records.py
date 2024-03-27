import flet as ft
from Config.config import supabase
import time


class ArtistsRecords(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  ============ the data table will be here ======= //
        self.artists_datatable = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("last name")),
                ft.DataColumn(ft.Text("email")),
                ft.DataColumn(ft.Text("phone number")),
                ft.DataColumn(ft.Text("gender")),
                ft.DataColumn(ft.Text("age")),
                ft.DataColumn(ft.Text("genre")),
                ft.DataColumn(ft.Text("residence")),
                ft.DataColumn(ft.Text("artist biography")),
            ],
            rows=[
            ]
        )
        self.fetch_all_artist_records()

    #  ================ // function to fetch the records in the database ======= //
    def fetch_all_artist_records(self):
        """Fetch all artist records from the database"""
        time.sleep(2)
        data, count = supabase.table("Artists").select("*").execute()
        if not data:
            print("no available records")
        else:
            data_tuple = data
            data_list = data_tuple[1]
            # ========== looping through the elements here
            for single_element in data_list:
                self.artists_datatable.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(single_element["first_name"])),
                            ft.DataCell(ft.Text(single_element["last_name"])),
                            ft.DataCell(ft.Text(single_element["email"])),
                            ft.DataCell(ft.Text(single_element["phone_number"])),
                            ft.DataCell(ft.Text(single_element["gender"])),
                            ft.DataCell(ft.Text(single_element["age"])),
                            ft.DataCell(ft.Text(single_element["genre"])),
                            ft.DataCell(ft.Text(single_element["residence"])),
                            ft.DataCell(ft.Text(single_element["artist_biography"])),
                        ]
                    )
                )


class Records(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.artists_records = ArtistsRecords(page=page)
        # ============ setting the whole page scroll
        self.page.scroll = ft.ScrollMode.HIDDEN
        #  ======== the fonts for the system will be here ======= //
        self.page.fonts = {
            "manrope": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "manrope-sem-bold": "assets/fonts/Manrope/static/Manrope-Regular.ttf",
            "manrop-bold": "assets/fonts/Manrope/static/Manrope-Bold.ttf"
        }
        #  =========== the content for the page will be here ========== //
        self.content = ft.Column(
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            expand=True,
                            gradient=ft.LinearGradient(
                                colors=[
                                    "#CBCCFF",
                                    "#CBCCFF"
                                ],
                                begin=ft.alignment.top_right,
                                end=ft.alignment.bottom_left,
                            ),
                            border_radius=ft.border_radius.all(10),
                            content=ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.ResponsiveRow(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Container(
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                margin=ft.margin.only(top=30),
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Text(
                                                                            "manage available artist records".capitalize(),
                                                                            size=30,
                                                                            font_family="manrop-bold",
                                                                            color="#212121"
                                                                        ),
                                                                        #  =========== the container for the table
                                                                    ]
                                                                )
                                                            ),

                                                            ft.Container(
                                                                content=ft.Row(
                                                                    scroll=ft.ScrollMode.ADAPTIVE,
                                                                    controls=[
                                                                        self.artists_records.artists_datatable
                                                                    ]
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                    col={"sm": 12, "md": 12, "lg": 12}
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            )
                        )
                    ]
                )
            ]
        )
