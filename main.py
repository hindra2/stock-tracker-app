from searchpage import SearchPage
from loginpage import LoginPage
from homepage import HomePage

# Flet imports
import flet
from flet import (
    UserControl,
    Page,
    View,
    AppBar,
    Text,
    Icon,
    Container,
    Column,
    Row,
    Text,
    ElevatedButton,
    TextField,
    VerticalDivider,
    NavigationRail,
    NavigationRailDestination,
    IconButton,
    alignment,
    padding,
    icons
)


def main(page:Page):
    page.title="StockAppIA"

    # Pages
    search_page = SearchPage(page)
    login_page = LoginPage(page)
    home_page = HomePage()

    # Navbar
    class NavBar(UserControl):
        def route_control(self, route):
            if route == 0:
                page.go("/home")
            elif route == 1:
                page.go("/search")
            elif route == 2:
                print("third")
            elif route == 3:
                print("fourth")
            elif route == 4:
                print("fifth")

        def build(self):
            return NavigationRail(
                min_width=100,
                min_extended_width=100,
                group_alignment=-0.9,
                destinations=[
                    NavigationRailDestination(
                        icon=icons.HOME_OUTLINED,
                        selected_icon=icons.HOME
                    ),
                    NavigationRailDestination(
                        icon=icons.ANALYTICS_OUTLINED,
                        selected_icon=icons.ANALYTICS
                    ),
                    NavigationRailDestination(
                        icon_content=Icon(icons.SHOPPING_CART_OUTLINED),
                        selected_icon_content=Icon(icons.SHOPPING_CART),
                    ),
                    NavigationRailDestination(
                        icon=icons.AUTO_STORIES_OUTLINED,
                        selected_icon_content=Icon(icons.AUTO_STORIES),
                    ),
                    NavigationRailDestination(
                        icon=icons.ACCOUNT_CIRCLE_OUTLINED,
                        selected_icon_content=Icon(icons.ACCOUNT_CIRCLE)
                    )
                ],
                on_change=lambda e: self.route_control(e.control.selected_index),
            )

    def page_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("LoginPage")),
                    login_page
                ],
            )
        )

        if page.route == "/home":
            page.views.append(
                View(
                    "/home",
                    [
                        AppBar(title=Text("HomePage")),
                        Row(
                            [
                                NavBar(),
                                VerticalDivider(width=1),
                                home_page
                            ],
                            expand=True,
                        )
                    ]
                )
            )
        elif page.route == "/search":
            page.views.append(
                View(
                    "/search",
                    [
                        AppBar(title=Text("SearchPage")),
                        Row(
                            [
                                NavBar(),
                                VerticalDivider(width=1),
                                search_page
                            ],
                            expand=True,
                        )
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = page_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    flet.app(target=main)