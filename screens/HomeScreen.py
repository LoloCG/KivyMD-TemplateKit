from kivymd.uix.screen import MDScreen

import os
from kivy.lang import Builder
kv_path = os.path.join(os.path.dirname(__file__), 'HomeScreen_layout.kv')
Builder.load_file(kv_path)

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen "{self.name}"')
    
    def on_enter(self):
        print(f'In screen "{self.name}"')
        self.manager.parent.ids.top_bar_title.text = "Home"

    def on_leave(self):
        print(f'Leaving {self.name}.')