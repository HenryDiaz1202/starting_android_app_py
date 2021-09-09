import time

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatIconButton
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import MDScreen
from kivy.app import App

Builder.load_string('''

<CameraClick>:
    orientation:'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Iniciar'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp' 
    Button: 
        text: 'Tomar foto'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        trimester = time.strftime("%Y%m%d_%%H%M%S")
        camera.export_to_png("IMG_{}.png".format(trimester))
        print("Captured")


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        screen = MDScreen()
        screen.add_widget(
            MDIcon(
                halign='center',
                icon="language-python",
                pos_hint={'x': 0, 'y': 0.3}
            )
        )
        screen.add_widget(
            MDLabel(
                text="Object recognition",
                pos_hint={'x': 0, 'y': 0.2},
                halign="center"
            )
        )
        screen.add_widget(
            MDRoundFlatIconButton(
                icon="camera",
                text="Abrir cámara",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        screen.add_widget(
            MDLabel(
                text="Developed by \n henrydiaz",
                pos_hint={"center_x": 0.5, "center_y": 0.2},
                halign="center"
            )
        )
        return screen


class Principal(App):
    def build(self):
        return CameraClick()


Principal().run()
