from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelHeader, MDExpansionPanelContent
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText
# from kivymd.uix.list import MDListItemHeadlineText, MDListItem

from kivy.uix.behaviors import ButtonBehavior

Builder.load_string("""
<ExpansionScreen>:
    name: "exp_panel_screen"
    size_hint: 1, 1

    MDScrollView:
        MDBoxLayout:
            id: container
            orientation: 'vertical'
            spacing: "5dp"
            # padding: "10dp"
            pos_hint: {"top": 1}
            adaptive_height: True

<MyPanelHeader>:
    orientation: "horizontal"
    size_hint_y: None
    height: "56dp"

    MDListItem:
        # ripple_effect: False
        md_bg_color: self.theme_cls.surfaceContainerLowColor
        on_release: root.on_release()

        MDListItemHeadlineText:
            id: header_text
            halign: "left"
""")

class MyPanelHeader(ButtonBehavior, MDExpansionPanelHeader):
    def __init__(self, text, panel, **kwargs):
        super(MyPanelHeader, self).__init__(**kwargs)
        self.ids.header_text.text = text
        self.panel = panel

    def on_release(self):
        if self.panel.is_open:
            self.panel.close()
        else:
            self.panel.open()
        print(f"clicked {self.ids.header_text.text}")

class ExpansionScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen {self.name}')

        example_panels = {
            "Panel 1": "Panel 1 content",
            "Panel 2": "Panel 2 content",
        }

        self.setup_panels(example_panels)
    
    def setup_panels(self, panels):

        for panel_title, panel_cont in panels.items():

            panel = MDExpansionPanel(
                orientation='vertical',
                pos_hint={"center_x": .5, "top": 1},
            )

            header = MyPanelHeader(
                text=panel_title,
                panel=panel,
            )
        
            content = MDExpansionPanelContent(
                MDLabel(
                    text=panel_cont,
                    adaptive_height=True,
                    padding=("16dp", "12dp"),
                ),
                md_bg_color= self.theme_cls.surfaceContainerLowestColor,
                padding=("16dp", "12dp"),
                orientation= "vertical",
            )

            panel.add_widget(header)
            panel.add_widget(content)

            self.ids.container.add_widget(panel)