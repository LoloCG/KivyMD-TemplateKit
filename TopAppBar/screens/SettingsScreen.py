from kivy.lang import Builder
SettingsScreen_layout = """
BoxLayout:
    orientation: 'vertical'
    MDLabel:
        text: "Settings Screen"
        halign: "center"
"""       
from kivymd.uix.screen import MDScreen

class SettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen {self.name}')

        print(f'Adding SettingsScreen layout')
        layout = Builder.load_string(SettingsScreen_layout)
        self.add_widget(layout)

    def on_enter(self):
        print(f'In screen {self.name}')
        self.manager.parent.ids.top_bar_title.text = "Settings"

    def on_leave(self):
        print(f'Leaving {self.name}.')