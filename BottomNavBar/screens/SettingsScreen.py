from kivy.lang import Builder
from kivy.app import App
from kivymd.uix.screen import MDScreen

SettingsScreen_layout = """
MDBoxLayout:
    name: "settings_screen"
    orientation: 'vertical'
    md_bg_color: self.theme_cls.secondaryContainerColor
    
    MDLabel:
        text: "Settings"
        halign: "center"
        pos_hint: {"top": 1}
        size_hint_y: None
        height: dp(56)
        padding: dp(10)

    ScrollView:
        id: scroll_container
        do_scroll_y: True
        adaptive_height: True
        bar_width: dp(10)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(15)
            padding: dp(20)
            pos_hint: {"top": 1}
            size_hint_y: None
            adaptive_height: True

            MDBoxLayout:
                orientation: 'horizontal'
                spacing: dp(10)
                size_hint_y: None
                height: dp(56)
                pos_hint: {'center_x': .5, 'center_y': .5}

                MDLabel:
                    text: "Auto-Detect Theme"
                    halign: "left"
                MDSwitch:
                    id: auto_detect_theme_switch
                    ripple_effect: False

            MDDivider:
                size_hint_x: .5
                pos_hint: {'center_x': .5, 'center_y': .5}

            MDBoxLayout:
                orientation: 'horizontal'
                spacing: dp(10)
                size_hint_y: None
                height: dp(56)
                pos_hint: {'center_x': .5, 'center_y': .5}
                
                MDLabel:
                    text: "Light/Dark Theme"
                    halign: "left"

                MDSwitch:
                    id: dark_mode_switch
                    disabled: auto_detect_theme_switch.active
                    ripple_effect: False
"""



class SettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen {self.name}')

        print(f'Adding SettingsScreen layout')
        layout = Builder.load_string(SettingsScreen_layout)
        self.add_widget(layout)

        layout.ids.auto_detect_theme_switch.bind(active=self.on_auto_detect_theme_changed)
        layout.ids.dark_mode_switch.bind(active=self.on_dark_mode_changed)

    def on_enter(self):
        print(f'In screen {self.name}')

    def on_leave(self):
        print(f'Leaving {self.name}.')
    def on_dark_mode_changed(self, instance, value):
        app = App.get_running_app()
        app.set_dark_mode(value)