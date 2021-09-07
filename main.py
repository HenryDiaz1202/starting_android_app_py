from kivy.app import App
from kivymd.theming import ThemeManager

class Main(App):
    theme_cls = ThemeManager()


Main().run()