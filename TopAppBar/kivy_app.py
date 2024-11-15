import os
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from screens.HomeScreen import HomeScreen
from screens.SettingsScreen import SettingsScreen

from kivy.lang import Builder

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.add_theme_and_palette()

        kv_path = os.path.join(os.path.dirname(__file__), 'main_layout.kv')
        self.root = Builder.load_file(kv_path)
        print(f"Loaded main_layout.kv file.")

        self.sm = self.root.ids.screen_manager
        
        self.add_screen("home_screen")

        return self.root

    def add_theme_and_palette(self):
        theme = "Dark"
        palette = "Pink" # "Olive", "Purple", "Red"
        self.theme_cls.theme_style = theme
        self.theme_cls.primary_palette = palette
        print(f"theme style = {theme}, primary_palette = {palette}")

    def add_screen(self, screen_name):
        if screen_name == "home_screen":
            self.sm.add_widget(HomeScreen(
                name="home_screen")
            )

        elif screen_name == "settings_screen":
            self.sm.add_widget(SettingsScreen(
                name="settings_screen")
            )

        print(f"Added {screen_name} to manager.")

    def on_stop(self):
        print("Closing KivyMD App.")

    def switch_screen(self, screen_name):     
        if self.sm.current == screen_name:
            print(f"Already in screen {screen_name}")
            return
        
        print(f"Switching to screen: {screen_name}")
        try:
            prev_screen = self.sm.current

            self.add_screen(screen_name)
            self.sm.current = screen_name

            if prev_screen:
                self.sm.remove_widget(self.sm.get_screen(prev_screen))
        
        except Exception as e:
            print(f"Error changing screen to '{screen_name}': {e}")
        
if __name__ == '__main__':
    MainApp().run()