import sys
import yfinance as yf
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class StockTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.stock_data = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(60000)  # update data every 60 seconds
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Stock Tracker")
        self.setGeometry(300, 300, 300, 150)

        # create widgets
        self.stock_code_label = QLabel("Stock Code:", self)
        self.stock_code_edit = QLineEdit(self)
        self.get_data_button = QPushButton("Get Data", self)
        self.get_data_button.clicked.connect(self.get_data)
        self.stock_price_label = QLabel("", self)

        # create layout
        layout = QVBoxLayout()
        layout.addWidget(self.stock_code_label)
        layout.addWidget(self.stock_code_edit)
        layout.addWidget(self.get_data_button)
        layout.addWidget(self.stock_price_label)
        self.setLayout(layout)

    def get_data(self):
        stock_code = self.stock_code_edit.text()
        self.stock_data = yf.Ticker(stock_code)
        self.update_data()

    def update_data(self):
        if self.stock_data is None:
            self.stock_price_label.setText("Please enter a stock code.")
            return
        stock_info = self.stock_data.info
        stock_price = stock_info["regularMarketPrice"]
        self.stock_price_label.setText(f"Current Price: ${stock_price}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    st = StockTracker()
    st.show()
    sys.exit(app.exec_())
