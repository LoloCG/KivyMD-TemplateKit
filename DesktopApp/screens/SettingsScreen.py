from kivy.app import App
from kivymd.uix.screen import MDScreen

import os
from kivy.lang import Builder
kv_path = os.path.join(os.path.dirname(__file__), 'SettingsScreen_layout.kv')
Builder.load_file(kv_path)

class SettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen {self.name}')
        
    # def on_kv_post(self, base_widget):
    #     app = App.get_running_app()
    #     theme_style = app.theme_cls.theme_style
    #     print(f"DEBUG: theme in settings set to {theme_style}")
        
    #     if theme_style == "Dark":
    #         self.ids.dark_mode_switch.active = True
    #     else:
    #         self.ids.dark_mode_switch.active = False

    def on_enter(self):
        print(f'In screen {self.name}')

    def on_leave(self):
        print(f'Leaving {self.name}.')