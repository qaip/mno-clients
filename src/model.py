from .database import Client


class Model:
    def __init__(self) -> None:
        self.clients: list[list[str]] = []
        self.checked: list[str] = []
        """
        A list of selected account numbers
        """
