from kivy.lang import Builder
Screen2_layout = """
BoxLayout:
    name: "second_screen"
    orientation: 'vertical'
    MDLabel:
        text: "Screen 2"
        halign: "center"
"""
Screen3_layout = """
BoxLayout:
    name: "third_screen"
    orientation: 'vertical'
    MDLabel:
        text: "Screen 3"
        halign: "center"
"""
from kivymd.uix.screen import MDScreen

class SecondScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen {self.name}')

        print(f'Adding SecondScreen layout')
        layout = Builder.load_string(Screen2_layout)
        self.add_widget(layout)

    def on_enter(self):
        print(f'In screen {self.name}')

    def on_leave(self):
        print(f'Leaving {self.name}.')

class ThirdScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen {self.name}')

        print(f'Adding SecondScreen layout')
        layout = Builder.load_string(Screen3_layout)
        self.add_widget(layout)

    def on_enter(self):
        print(f'In screen {self.name}')

    def on_leave(self):
        print(f'Leaving {self.name}.')