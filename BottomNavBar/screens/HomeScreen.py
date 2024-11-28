from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

import os
from kivy.lang import Builder
kv_path = os.path.join(os.path.dirname(__file__), 'HomeScreen_layout.kv')
Builder.load_file(kv_path)

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen "{self.name}"')

    def on_pre_enter(self):
        app = MDApp.get_running_app()
        app.progress_bar(start=False)

    def on_enter(self):
        print(f'In screen "{self.name}"')        

    def on_leave(self):
        print(f'Leaving {self.name}.')