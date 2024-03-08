import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#fafafa"
    page.window_center()
    page.window_min_width = 768

    # ============= the function for the routing will be here ======== //
    def router(route):
        try:
            page.views.clear() # === removing the fault bahaviour
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            page.snack_bar.open = True
            page.update()
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
