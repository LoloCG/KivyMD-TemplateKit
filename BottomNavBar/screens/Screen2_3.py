from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

from kivymd.uix.label import MDLabel
from kivymd.uix.tab import (
    MDTabsItem,
    MDTabsItemText
)

Builder.load_string("""
<SecondScreen>:
    name: "second_screen"

    MDTabsPrimary:
        id: main_tabs
        pos_hint: {"center_x": .5, "top": 1}
        label_only: True

        MDDivider:
        
        MDTabsCarousel:
            id: tabs_content_container
            size_hint_y: None
            height: root.height - main_tabs.ids.tab_scroll.height
            lock_swiping: True

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

    def on_pre_enter(self):
        # If there are tabs present, dont set up any of them
        if self.ids.main_tabs.get_tabs_list(): 
            return

        tab_list = ["Tab 1", "Tab 2", "Tab 3", "Tab 4", "Tab 5"]
        self.setup_tabs(tab_list)

    def setup_tabs(self, tab_list):
        print(f"Creating tabs.")
        try:
            for tab_name in tab_list:
            
                new_tab = MDTabsItem(
                    MDTabsItemText(
                        text=tab_name
                    )
                )

                self.ids.main_tabs.add_widget(new_tab)

                self.ids.tabs_content_container.add_widget(
                    # TODO: this could be substituted with a scrollview with an ID,
                        # acting as the container for the expansionPanels sessions
                        # which could be defined in a separate class
                    MDLabel(
                        text=tab_name,
                        halign="center",
                    )
                )
                            
            self.ids.main_tabs.switch_tab(text=tab_list[0])

        except Exception as e:
            print(f"Error in setup_tabs: {e}")

    def on_enter(self):
        app = MDApp.get_running_app()
        app.progress_bar(start=False)
        print(f"Entered HomeScreen.")

    def on_pre_leave(self):
        pass
        # print("clearing main_tabs widgets")
        # self.ids.main_tabs.clear_widgets()

    def on_leave(self):
        print(f'Leaving {self.name}.')

        # Enabling the clearing of tabs causes error of them not reappearing when 
            # returning back to home_screen, returning at random.
            # Maybe its due to MDTabsPrimary being in the KV file?
        # self.clear_widgets()

class ThirdScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen {self.name}')

    def on_enter(self):
        print(f'In screen {self.name}')

    def on_leave(self):
        print(f'Leaving {self.name}.')