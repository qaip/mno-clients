from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp


from .controller import Controller


class View(MDScreenManager):
    def __init__(self, controller: Controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.table = self.Table()
        self.screen = self.Screen()
        self.add_widget(self.screen)

    def Screen(self):
        return MDScreen(
            MDTopAppBar(
                id="bar",
                title="MNO Clients",
                elevation=0,
                pos_hint={"top": 1, "left": 0},
                size=(200, 100),
                size_hint=(1, None),
            ),
            self.table,
            MDRectangleFlatButton(
                text="Filter",
                size=(25, 25),
                pos_hint={"center_x": 0.93, "top": 0.98},
                font_size=20,
                md_bg_color=(0.5, 0.5, 0.5, 1),
                text_color=(1, 1, 1, 1),
                on_press=self.controller.open_filter_dialog,
            ),
            MDRectangleFlatButton(
                text="Add",
                size=(25, 25),
                pos_hint={"center_x": 0.825, "top": 0.98},
                font_size=20,
                md_bg_color=(0.5, 0.5, 0.5, 1),
                text_color=(1, 1, 1, 1),
                on_press=self.controller.open_add_dialog,
            ),
            MDRectangleFlatButton(
                text="Delete",
                size=(25, 25),
                pos_hint={"center_x": 0.713, "top": 0.98},
                font_size=20,
                md_bg_color=(0.5, 0.5, 0.5, 1),
                text_color=(1, 1, 1, 1),
                on_press=self.controller.open_delete_dialog,
            ),
            name="table",
            id="table",
        )

    def Table(self):
        table = MDDataTable(
            padding=(0, 70, 0, 0),
            elevation=0,
            check=True,
            use_pagination=True,
            pagination_menu_height=300,
            column_data=[
                ("Name", dp(35)),
                ("Account", dp(25)),
                ("Address", dp(30)),
                ("Mobile phone", dp(30)),
                ("Landline", dp(30)),
            ],
        )
        table.bind(on_check_press=self.controller.toggle_check)
        return table

    def AddClientDialog(self):
        return MDDialog(
            title="Client",
            type="custom",
            on_dismiss=lambda _: True,
            content_cls=MDBoxLayout(
                MDTextField(
                    id="name",
                    hint_text="Name",
                    font_size="20",
                    helper_text="This field is required",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id="account_number",
                    hint_text="Account number",
                    font_size="20",
                    max_text_length=5,
                    helper_text="Please provide a valid account number",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id="address",
                    hint_text="Address",
                    font_size="20",
                    helper_text="Please provide a valid address",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id="mobile_phone",
                    hint_text="Mobile phone",
                    font_size="20",
                    helper_text="Please provide a valid phone number",
                    helper_text_mode="on_error"

                ),
                MDTextField(
                    id="landline",
                    hint_text="Landline",
                    font_size="20",
                    helper_text="Please provide a valid landline number",
                    helper_text_mode="on_error"
                ),
                id="add_dialog",
                orientation="vertical",
                spacing="15dp",
                size_hint_y=None,
                height="370dp"
            ),
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    on_release=self.controller.close_dialog
                ),
                MDFlatButton(
                    text="Add",
                    theme_text_color="Custom",
                    on_release=self.controller.add
                ),
            ],
        )

    def FilterClientDialog(self):
        return MDDialog(
            title="Filter clients",
            type="custom",
            on_dismiss=lambda _: True,
            content_cls=MDBoxLayout(
                MDTextField(
                    id="name",
                    hint_text="Name",
                    font_size="20",
                ),
                MDTextField(
                    id="phone",
                    hint_text="Mobile phone or landline number",
                    font_size="20",
                ),
                id="add_dialog",
                orientation="vertical",
                spacing="15dp",
                size_hint_y=None,
                height="140dp"
            ),
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    on_release=self.controller.close_dialog
                ),
                MDFlatButton(
                    text="Filter",
                    theme_text_color="Custom",
                    on_release=self.controller.filter
                ),
            ],
        )

    def DeleteClientsDialog(self, count: int):
        return MDDialog(
            title=f"Are you sure you want to delete {count} client{'' if count == 1 else 's'}?",
            type="custom",
            on_dismiss=lambda _: True,
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    font_style="Button",
                    on_release=self.controller.close_dialog
                ),
                MDFlatButton(
                    text="Confirm",
                    font_style="Button",
                    on_release=self.controller.delete
                ),
            ],
        )

    def InfoDialog(self, message: str):
        return MDDialog(
            title=message,
            type="custom",
            on_dismiss=lambda _: True,
            buttons=[
                MDFlatButton(
                    text="Ok",
                    font_style="Button",
                    on_release=self.controller.close_dialog
                ),
            ],
        )
