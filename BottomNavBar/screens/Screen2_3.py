from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_string("""
<SecondScreen>:
    size_hint: 1, 1

    BoxLayout:
        name: "second_screen"
        orientation: 'vertical'

        MDLabel:
            text: "Screen 2"
            halign: "center"

        MDButton:
            style: "elevated"
            pos_hint: {'center_x': 0.5}
            on_release: print("Button of screen 2 pressed.")

            MDButtonText:
                text: "Screen 2 button"

        Widget:

<ThirdScreen>:
    size_hint: 1, 1

    BoxLayout:
        name: "third_screen"
        orientation: 'vertical'

        MDLabel:
            text: "Screen 3"
            halign: "center"

        MDButton:
            style: "elevated"
            pos_hint: {'center_x': 0.5}
            on_release: print("Button of screen 3 pressed.")

            MDButtonText:
                text: "Screen 3 button"

        Widget:
""")

class SecondScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen {self.name}')

    def on_enter(self):
        print(f'In screen {self.name}')

    def on_leave(self):
        print(f'Leaving {self.name}.')

class ThirdScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen {self.name}')

    def on_enter(self):
        print(f'In screen {self.name}')

    def on_leave(self):
        print(f'Leaving {self.name}.')