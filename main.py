import flet as ft
from Views.dashboard import Dashboard


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.window_center()
    page.window_min_width = 768
    page.window_min_height = 700
    page.scroll = ft.ScrollMode.ADAPTIVE

    # ============= the function for the routing will be here ======== //
    # Define a method to handle page routing
    def router(route):
        page.views.clear()

        if page.route == "/dashboard":
            landing = Dashboard(page=page)
            page.views.append(landing)

        page.update()

    page.on_route_change = router
    page.go("/dashboard")


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
