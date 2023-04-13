from kivymd.app import MDApp
import os

from .view import View


class App(MDApp):
    def __init__(self, **kwargs):
        from .database import Database
        from .controller import Controller
        from .model import Model

        super().__init__(**kwargs)
        self.model = Model()
        self.database = Database()
        self.controller = Controller(self)

    def terminate_app(self):
        self.stop()

    def build(self):
        from .view import View
        self.view = View(self.controller)

        self.title = 'MNO clients'
        self.theme_cls.primary_palette = "Gray"
        self.view.current = "table"
        self.controller.update_clients()

        return self.view
