from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatIconButton
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import MDScreen


class ActivarReconocimiento(MDApp):
    def build(self):
        screen = MDScreen()
        screen.add_widget(
            MDLabel(
                text="Object recognition",
                pos_hint={'x': 0, 'y': 0.2},
                halign="center"
            )
        )
        screen.add_widget(
            Button(text="Hello")
        )
        return screen


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


MainApp().run()