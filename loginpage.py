from flet import (
    UserControl,
    Container,
    Column,
    Row,
    Text,
    ElevatedButton,
    TextField,
    alignment,
    colors,
    margin,
    padding,
    Page
)
from flet.ref import Ref
from login import Login


class LoginPage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.username = Ref[TextField]()
        self.password = Ref[TextField]()
        self.page = page

    def login(self, e):
        self.page.go("/home")

    def build(self):
        # compiling all in one container
        return Container(
            alignment=alignment.center,
            content=Container(
                padding=padding.symmetric(vertical=200),
                width=600,
                alignment=alignment.center,
                content=Column([
                        Row(
                            controls=[
                                TextField(
                                    ref=self.username,
                                    label="Username",
                                    hint_text="Enter here",
                                    expand=1,
                                )
                            ]
                        ),
                    Row(
                            controls=[
                                TextField(
                                    ref=self.password,
                                    label="Password",
                                    hint_text="Enter here",
                                    password=True,
                                    can_reveal_password=True,
                                    expand=1
                                )
                            ]
                    ),
                    Row(
                        alignment="center",
                        controls=[
                            ElevatedButton(
                                text="Login",
                                width=400,
                                on_click=self.login
                            )
                        ]
                    )
                ])
            )
        )