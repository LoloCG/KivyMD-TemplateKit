from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelHeader, MDExpansionPanelContent
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText

Builder.load_string("""
<ExpansionScreen>:
    size_hint: 1, 1
    name: "exp_panel_screen"

    MDBoxLayout:
        size_hint: 1, 1    
        id: container
        orientation: 'vertical'
""")

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
            header = MDExpansionPanelHeader(
                MDButton(
                    MDButtonText(
                        text=panel_title,
                    ),
                    style="filled",
                    radius=["5dp","5dp", "5dp", "5dp"],
                    size_hint=(1, None),
                    height="56dp",
                ),
            )
        
            content = MDExpansionPanelContent(
                MDLabel(
                    text=panel_cont,
                    adaptive_height=True,
                ),
                orientation= "vertical",
            )

            panel = MDExpansionPanel(
                orientation='vertical',
                size_hint=(1, 1),
            )
            panel.add_widget(header)
            panel.add_widget(content)

            self.ids.container.add_widget(panel)
