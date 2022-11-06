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
    padding,
    AlertDialog,
    TextButton,
    Icon,
    icons,
    Banner
)
from flet.ref import Ref
from stock import Stock

class SearchPage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.ticker = Ref[TextField]()
        self.info = Ref[Column]()
        self.page = page
        self.error_alert = AlertDialog(title=Text("Error: Input an actual ticker name!"))

    def getStockInfo(self, e):
        try:
            stock = Stock(self.ticker.current.value)
            opening_price = stock.getOpeningPrice()
            price_range = stock.getPriceRange()
            volume = stock.getVolume()
            name = stock.getName()

            self.info.current.controls.append(
                Text(f"{self.ticker.current.value}\n{opening_price}\n{price_range}\n{volume}\n{name}")
            )
            self.ticker.current.value = ""
            self.update()

        except KeyError:
            self.ticker.current.value = ""
            self.page.dialog = self.error_alert
            self.page.dialog.open = True
            self.page.update()

    def build(self):
        return Container(
            width=900,
            alignment=alignment.center,
            content=Column([
                Row(
                    controls=[
                        TextField(
                        ref=self.ticker,
                        label="Ticker",
                        hint_text="Enter here",
                        ),
                        ElevatedButton(
                            "Submit",
                            on_click=self.getStockInfo
                        )
                    ],
                ),
                Column(ref=self.info)
            ])
        )
