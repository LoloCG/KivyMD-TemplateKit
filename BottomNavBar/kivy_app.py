import os
from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager # not using MDScreenManager as i wont be using heroes
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer
from kivymd.uix.button import MDButton, MDButtonText

from screens.HomeScreen import HomeScreen
from screens.SettingsScreen import SettingsScreen
from screens.Screen2_3 import SecondScreen, ThirdScreen

from kivy.lang import Builder

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_history = []

    def build(self):
        self.add_theme_and_palette()

        kv_path = os.path.join(os.path.dirname(__file__), 'main_layout.kv')
        self.root = Builder.load_file(kv_path)
        print(f"Loaded main_layout.kv file.")

        self.sm = self.root.ids.screen_manager

        self.add_screen("home_screen")

        return self.root

    def add_screen(self, screen_name):
        if screen_name == "home_screen":
            self.sm.add_widget(HomeScreen(
                name="home_screen")
            )

        elif screen_name == "settings_screen":
            self.sm.add_widget(SettingsScreen(
                name="settings_screen")
            )

        elif screen_name == "second_screen":
            self.sm.add_widget(SecondScreen(
                name="second_screen")
            )

        elif screen_name == "third_screen":
            self.sm.add_widget(ThirdScreen(
                name="third_screen")
            )

        print(f"Added {screen_name} to manager.")

    def on_stop(self):
        print("Closing KivyMD App.")

    # ========================= Related to Styling =========================

    def add_theme_and_palette(self):
        palette = "Blue" # "Olive", "Purple", "Red"

        self.theme_cls.primary_palette = palette

        print(f"Primary_palette = {palette}")

    def set_dark_mode(self, value):
        print(f"Setting dark mode to {'ON' if value else 'OFF'}")
        self.theme_cls.theme_style = "Dark" if value else "Light"

    # ========================= Related to Screen changes =========================
    def switch_screen(self, screen_name):
        prev_screen = self.sm.current  
        if prev_screen == screen_name:
            print(f"Already in screen {screen_name}")
            return
        
        print(f"Switching to screen: {screen_name}")
        try:
            self.add_screen(screen_name)
            self.sm.current = screen_name

            if prev_screen:
                self.sm.remove_widget(self.sm.get_screen(prev_screen))
                if prev_screen not in self.screen_history:
                    self.screen_history.append(prev_screen)
            
            self.update_back_button()

        except Exception as e:
            print(f"Error changing screen to '{screen_name}': {e}")
    
    def go_back_screen(self):
        if not self.screen_history:
            print("No screens in history.")
            return
        
        recent_screen = self.sm.current

        previous_screen = self.screen_history.pop()
        print(f"Going back to screen: {previous_screen}")

        # Add the screen if it's not already in the ScreenManager
        if not self.sm.has_screen(previous_screen):
            self.add_screen(previous_screen)

        self.sm.current = previous_screen
        self.sm.remove_widget(self.sm.get_screen(recent_screen))

        self.update_back_button()

    def update_back_button(self):
        back_leading_button = self.root.ids.back_leading_button
        if len(self.screen_history) == 0:
            back_leading_button.disabled = True 
            back_leading_button.icon = ""
        else:
            back_leading_button.disabled = False
            back_leading_button.icon = "chevron-left"

    # ========================= Related to Menus and Dialogs =========================
    def open_top_menu(self, button):
        menu_items = [{
                "text": "Settings",
                "leading_icon": "cog",
                "on_release": lambda x="settings_screen": self.switch_screen(x)
            },
            {
                "text": "About",
                "leading_icon": "help-circle-outline",
                "on_release": lambda x=None: self.open_about_dialog(),
            },
        ]

        menu = MDDropdownMenu(
            caller=self.root.ids.dots_menu,
            items=menu_items,
            position="auto",
        )
        menu.open()

    def open_about_dialog(self):
        about_dialog = MDDialog(
            MDDialogHeadlineText(
                text="About",
                halign="left",
            ),
            MDDialogSupportingText(
                text="""Kivy/KivyMD template application created for rapid development of mobile apps with python.
                \nThis version displays Bottom Navigation bar + Top Application Bar, with basic settings menu.
                """,
                halign="left",
            ),
            MDDialogButtonContainer(
                MDButton(
                    MDButtonText(text="Return"),
                    style="text",
                    on_release=lambda x: about_dialog.dismiss(),
                ),
            ),
        )
        about_dialog.open()

if __name__ == '__main__':
    MainApp().run()