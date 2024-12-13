from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

from kivy.metrics import dp
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelHeader, MDExpansionPanelContent
from kivymd.uix.list import MDListItem 
from kivy.uix.behaviors import ButtonBehavior

Builder.load_string("""
<ExpansionScreen>:
    name: "exp_panel_screen"
    size_hint: 1, 1

    MDScrollView:
        do_scroll_x: False
        MDBoxLayout:
            id: scrollview_container
            orientation: 'vertical'
            # spacing: "5dp"
            # padding: "10dp"
            pos_hint: {"top": 1}
            adaptive_height: True

<ButtonPanelHeader>:
    orientation: "horizontal"

    MDListItem:
        md_bg_color: self.theme_cls.surfaceContainerLowColor
        on_release: root.on_release()
        divider: True
        size_hint_y: None
        height: "56dp"

        MDListItemSupportingText:
            id: header_text_left
            halign: "left"

        MDListItemTrailingSupportingText:
            id: header_text_right
            halign: "right"

<CustomPanelContent>:
    md_bg_color: self.theme_cls.surfaceContainerLowestColor
    orientation: 'vertical'

    MDBoxLayout:
        id: panel_content_layout
        orientation: 'vertical'
        pos_hint: {"top": 1.0}
        # adaptive_height: True
        padding: 0, "12dp" #
        size_hint_y: None

    MDDivider:
        pos_hint: {'center_x': .5, 'center_y': .5}

<ContentItem>:
    size_hint_y: None
    height: "56dp"

    MDListItemSupportingText:
        id: item_text
""")

class ButtonPanelHeader(ButtonBehavior, MDExpansionPanelHeader):
    """
        ButtonPanelHeader<MDExpansionPanel<(MDBoxLayout<MDScrollView<MDScreen)
    """
    def __init__(self, left_text, right_text, panel, **kwargs):
        super(ButtonPanelHeader, self).__init__(**kwargs)

        self.ids.header_text_left.text = left_text
        self.ids.header_text_right.text = right_text

        self.panel = panel

    def on_release(self):
        if self.panel.is_open:
            self.panel.close()
        else:
            self.panel.open()

class CustomPanelContent(MDExpansionPanelContent):
    def __init__(self, **kwargs):
        super(CustomPanelContent, self).__init__(**kwargs)
        pass

class ContentItem(MDListItem):
    def __init__(self, text, **kwargs):
        super(ContentItem, self).__init__(**kwargs)
        self.ids.item_text.text = text

class ExpansionScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen {self.name}')
        
        example_data = {
            '1':{
                'leading_text':'tab 1',
                'trailing_text': '1',
                'n_content_item': 3
            },
            '2':{
                'leading_text':'tab 2',
                'trailing_text': '2',
                'n_content_item': 3
            },
            '3':{
                'leading_text':'tab 3',
                'trailing_text': '3',
                'n_content_item': 3
            },
        }
        self.setup_panels(example_data)
    
    def setup_panels(self, example_data):
        """
        """
        for tab, tab_dict in example_data.items():
            panel = MDExpansionPanel(
                orientation='vertical',
                pos_hint={"center_x": .5, "top": 1},
                size_hint_y=None,
            )

            header = self.build_header(tab, tab_dict, panel)

            content = self.build_content(tab_dict)

            panel.add_widget(header)
            panel.add_widget(content)

            self.ids.scrollview_container.add_widget(panel)

    def build_header(self, tab, tab_dict, panel):
        header = ButtonPanelHeader(
            left_text=tab_dict.get("leading_text", tab), 
            right_text=tab_dict.get("trailing_text", " "),
            panel=panel,
        )
        return header

    def build_content(self, tab_dict):
        content_box = CustomPanelContent()
        
        total_height = 0
        for i in range(1, tab_dict['n_content_item']+1):
             
            content_box.ids.panel_content_layout.add_widget(
                ContentItem(text=f"item {i}")
                )

            # This value modifies the height of the ExpansionPanelContent
            total_height += 95
        
        total_height = dp(total_height)
        content_box.ids.panel_content_layout.height = total_height
        return content_box 
