import sys
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QSize

from geo.geo import *
from config import *

class GeoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.is_clicked = False

        self.scroll_area = QScrollArea()        # Scroll Area which contains the widgets, set as the centralWidget
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.button = QPushButton('Press to geo')
        self.button.clicked.connect(self.geo_response)
        self.vbox.addWidget(self.button)

        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)


        self.geo_lat = QTextEdit('Enter lat')
        self.geo_lon = QTextEdit('Enter lon')
        self.radius = QTextEdit('Enter lon')
        self.abox = QHBoxLayout()
        
        self.abox.addWidget(self.geo_lat)
        self.abox.addWidget(self.geo_lon)
        self.abox.addWidget(self.radius)
        self.vbox.addLayout(self.abox)

        self.setLayout(self.vbox)
        self.setWindowTitle('Geo')
        self.resize(800, 600)

    
    def geo_response(self):
        if not self.is_clicked:
            dadata = Dadata(DADATA_TOKEN)
            lon = 37.359486
            lat = 55.601983
            radius = 1000
            max_count = 20
            response = dadata_get_addresses(dadata, lat, lon, radius, max_count)
            adresses = addresses_to_json(response)

            self.add_adress_to_scroll_area(adresses['adresses'])
            self.is_clicked = True


    def add_adress_to_scroll_area(self, adresses):
        self.vbox.removeWidget(self.button)
        self.button.deleteLater()
        for adress in adresses:
            vb = QHBoxLayout()
            vb.addWidget(QLabel('Почтовый индекс: ' + adress['postal_code']))
            vb.addWidget(QLabel('Cтрана: ' + adress['country']))
            vb.addWidget(QLabel('Город: ' + adress['city']))
            vb.addWidget(QLabel('Дом: ' + adress['house']))
            vb.addWidget(QLabel('Широта: ' + adress['geo_lat']))
            vb.addWidget(QLabel('Долгота: ' + adress['geo_lon']))
            self.vbox.addLayout(vb)


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.is_clicked = False
        self.geo = None
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.hbox = QHBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        
        self.button_geo = QPushButton('To geo')
        self.button_geo.clicked.connect(self.to_geo)
        self.hbox.addWidget(self.button_geo)
        
        self.button_tg = QPushButton('To tg')
        self.button_tg.clicked.connect(self.to_tg)
        self.hbox.addWidget(self.button_tg)
        
        self.button_vk = QPushButton('To vk')
        self.button_vk.clicked.connect(self.to_vk)
        self.hbox.addWidget(self.button_vk)
        

        self.widget.setLayout(self.hbox)

        self.setCentralWidget(self.widget)
        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Волчий тон')
    
    def to_geo(self):
        if self.geo is None:
            self.geo = GeoWindow()
        self.geo.show()
    
    def to_tg(self):
        print('in progress')

    def to_vk(self):
        print('in progress')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyMainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
