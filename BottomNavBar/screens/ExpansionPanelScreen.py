from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelHeader, MDExpansionPanelContent
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.list import MDListItemSupportingText, MDListItem
from kivymd.uix.divider import MDDivider
from kivy.uix.behaviors import ButtonBehavior

Builder.load_string("""
<ExpansionScreen>:
    name: "exp_panel_screen"
    size_hint: 1, 1

    MDScrollView:
        do_scroll_x: False
        MDBoxLayout:
            id: container
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
        id: content_layout
        orientation: 'vertical'
        pos_hint: {"top": 1.0}
        # adaptive_height: True
        padding: 0, "12dp" #
        size_hint_y: None

    MDDivider:
        pos_hint: {'center_x': .5, 'center_y': .5}

<ExerciseItem>:
    size_hint_y: None
    height: "56dp"
    
    MDListItemSupportingText:
        text: "Exercise X"
""")

class ButtonPanelHeader(ButtonBehavior, MDExpansionPanelHeader):
    """
        Header should contain the name (if any), and the date (obligatory).
        If name is None, it should use the session id number.
    """
    def __init__(self, left_text, right_text, panel, **kwargs):
        super(ButtonPanelHeader, self).__init__(**kwargs)

        self.ids.header_text_left.text = left_text
        self.ids.header_text_right.text = right_text

        self.panel = panel

    def on_release(self):
        # print(f"clicked {self.ids.header_text.text}")
        if self.panel.is_open:
            self.panel.close()
        else:
            self.panel.open()
        
class CustomPanelContent(MDExpansionPanelContent):
    def __init__(self, **kwargs):
        super(CustomPanelContent, self).__init__(**kwargs)
        pass

class ExerciseItem(MDListItem):
    def __init__(self, **kwargs):
        super(ExerciseItem, self).__init__(**kwargs)


class ExpansionScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Loading screen {self.name}')
        self.microcycle = None
        
        raw_basic_data = {
            "timestamp": "2024-12-05 16:59:30",
            "mesocycle_length": 6,
            "days_length": 6,
            "mesocycle_name": "Mesocycle test",
            "mesocycle_ID": "bb44b864e3949295",
            "start_date": "2024-09-16",
            "microcycles_list": {
                "1": {
                    "1": {
                        "name": "A",
                        "date": "2024-09-16",
                        "microcycle_distribution": 1,
                        "session_timing": 0,
                        "n_exer": 3
                    },
                    "2": {
                        "name": "B",
                        "date": "2024-09-18",
                        "microcycle_distribution": 3,
                        "session_timing": 0,
                        "n_exer": 3
                    },
                    "3": {
                        "name": "A",
                        "date": "2024-09-20",
                        "microcycle_distribution": 5,
                        "session_timing": 0,
                        "n_exer": 3
                    }
                },
                "2": {
                    "4": {
                        "name": "B",
                        "date": "2024-09-22",
                        "microcycle_distribution": 1,
                        "session_timing": 0,
                        "n_exer": 3
                    },
                    "5": {
                        "name": "A",
                        "date": "2024-09-24",
                        "microcycle_distribution": 3,
                        "session_timing": 0,
                        "n_exer": 3
                    },
                    "6": {
                        "name": "B",
                        "date": "2024-09-26",
                        "microcycle_distribution": 5,
                        "session_timing": 0,
                        "n_exer": 3
                    }
                },
            }
        }

        selected_microcycle = 1

        basic_microcycle_data = self.clean_basic_data(raw_basic_data, selected_microcycle)

        self.setup_panels(basic_microcycle_data)
    
    def setup_panels(self, basic_microcycle_data):
        """
            {'1': {'name': 'A', 'date': '2024-09-16', 'n_exer': 3}, 
            '2': {'name': 'B', 'date': '2024-09-18', 'n_exer': 3}, 
            '3': {'name': 'A', 'date': '2024-09-20', 'n_exer': 3}}
        """
        for session, session_dict in basic_microcycle_data.items():
            print(f"Setting up session {session} panel.")

            panel = MDExpansionPanel(
                orientation='vertical',
                pos_hint={"center_x": .5, "top": 1},
                size_hint_y=None,
            )

            header = self.build_header(session, session_dict, panel)

            content = self.build_content(session_dict) # , cont_height

            # panel.bind(is_open=lambda instance, is_open: self.animate_panel(instance, is_open))

            panel.add_widget(header)
            panel.add_widget(content)

            # panel.height = cont_height

            self.ids.container.add_widget(panel)

    def build_header(self, session, session_dict, panel):
        left_text = session_dict.get("name", session)
        right_text = session_dict.get("date", " ")
        left_text = "Session " + left_text

        header = ButtonPanelHeader(
            left_text=left_text, 
            right_text=right_text,
            panel=panel,
        )
        return header

    def animate_panel(self, panel, is_open):
        from kivy.animation import Animation
        Animation(
            padding=[0, 12, 0, 12] if not is_open else [0, 0, 0, 0],
            d=0.2,
        ).start(panel)

    def build_content(self, session_dict):
        content_box = CustomPanelContent()
        
        total_height = 0
        for i in range(1, session_dict['n_exer']+1):
             
            content_box.ids.content_layout.add_widget(ExerciseItem())

            total_height += 95
        
        total_height = dp(total_height)
        content_box.ids.content_layout.height = total_height
        return content_box 

    def clean_basic_data(self, raw_basic_data, selected_microcycle):
        """
        "timestamp": "2024-12-05 16:59:30",
        "mesocycle_length": 6,
        "days_length": 6,
        "mesocycle_name": "Mesocycle test",
        "mesocycle_ID": "bb44b864e3949295",
        "start_date": "2024-09-16",
        "microcycles_list": {
            "1": {
                "1": {
                    "name": "A",
                    "date": "2024-09-16",
                    "microcycle_distribution": 1,
                    "session_timing": 0,
                    "n_exer": 3
                },
                "2": {
                    "name": "B",
                    "date": "2024-09-18",
                    "microcycle_distribution": 3,
                    "session_timing": 0,
                    "n_exer": 3
                },
                "3": {
                    "name": "A",
                    "date": "2024-09-20",
                    "microcycle_distribution": 5,
                    "session_timing": 0,
                    "n_exer": 3
                }
            },
            "2": {
                "4": {
                    "name": "B",
                    "date": "2024-09-22",
                    "microcycle_distribution": 1,
                    "session_timing": 0,
                    "n_exer": 3
                },
                "5": {
                    "name": "A",
                    "date": "2024-09-24",
                    "microcycle_distribution": 3,
                    "session_timing": 0,
                    "n_exer": 3
                },
                "6": {
                    "name": "B",
                    "date": "2024-09-26",
                    "microcycle_distribution": 5,
                    "session_timing": 0,
                    "n_exer": 3
                }
            },
        }
        best option to do:
            for this module of expansion panels, clean the data to obtain:
                all microcycles, all sessions, name, date, session_timing and n_exer.
                This will be saved for later lazyloading.
            Out of these, setup_panels will use the selected microcycle to generate the 
                template of sessions with each their name and date, and the exercises 
                to later be filled with complete data.
        """
        basic_microcycle_data = {}
        for microcycle, microcycle_dict in raw_basic_data["microcycles_list"].items():

            for session, session_dict in microcycle_dict.items():
                # print(f"\t{session}:")
                basic_microcycle_data[session] = {}

                for attr, value in session_dict.items():
                    if attr not in ["name", "date", "n_exer"]:
                        continue
                    basic_microcycle_data[session][attr] = value
                    # print(f"\t- {attr} - {value}")

            if microcycle == str(selected_microcycle):
                break
        return basic_microcycle_data