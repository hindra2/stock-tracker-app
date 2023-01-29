from flet import (
    UserControl,
    Container,
    Column,
    Row,
    Text,
    TextField,
    alignment,
    colors,
    Page,
    VerticalDivider,
    ElevatedButton,
    Page,
    padding
)
from flet.ref import Ref

class HomePage(UserControl):

    def build(self):
        return Column([
            Row(
                controls=[
                    Text("Hello World")
                ]
            ),
        ])
