from __future__ import annotations
from re import match
from .database import Client

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .app import App


class Controller:
    def __init__(self, app: App):
        self.app = app

    def update_clients(self, clients: list[Client] | None = None):
        if clients is None:
            clients = self.app.database.get_clients()
        self.app.model.clients = list(map(lambda client: [
            str(client.name),
            str(client.account_number),
            str(client.address),
            str(client.mobile_phone),
            str(client.landline)
        ], clients))
        self.app.view.table.row_data = self.app.model.clients

    def toggle_check(self, table, row: list[str]):
        account_number = row[1]
        if account_number in self.app.model.checked:
            self.app.model.checked.remove(account_number)
        else:
            self.app.model.checked.append(account_number)

    def open_add_dialog(self, event):
        self.dialog = self.app.view.AddClientDialog()
        self.dialog.open()

    def open_filter_dialog(self, event):
        self.dialog = self.app.view.FilterClientDialog()
        self.dialog.open()

    def open_delete_dialog(self, event):
        count = len(self.app.model.checked)
        self.dialog = self.app.view.DeleteClientsDialog(count)
        self.dialog.open()

    def close_dialog(self, event=None):
        self.dialog.dismiss(force=True)

    def filter(self, event):
        criteria = self.dialog.content_cls.ids
        result = self.app.database.get_filter_result(
            name=criteria.name.text,
            phone=criteria.phone.text,
        )
        self.close_dialog()
        self.update_clients(result)

    def delete(self, event):
        num_deleted = self.app.database.delete_clients(self.app.model.checked)
        self.close_dialog()
        message = f"Successfully deleted {num_deleted} client{'' if num_deleted == 1 else 's'}"
        self.update_clients()
        self.dialog = self.app.view.InfoDialog(message)
        self.dialog.open()

    def add(self, event):
        client_data = self.dialog.content_cls.ids
        if self.validate_client(client_data):
            client = Client(
                name=client_data.name.text,
                account_number=client_data.account_number.text,
                address=client_data.address.text,
                mobile_phone=client_data.mobile_phone.text,
                landline=client_data.landline.text,
            )
            self.app.database.add_client(client)
            self.update_clients()
            self.close_dialog()
            message = f"Successfully added a new client"
            self.dialog = self.app.view.InfoDialog(message)
            self.dialog.open()

    def validate_client(self, client):
        if not client.name.text or len(client.name.text) < 3:
            client.name.error = True
            return False
        if not client.account_number.text or len(client.account_number.text) != 5:
            client.account_number.error = True
            return False
        if not client.address.text or len(client.address.text) < 4:
            client.address.error = True
            return False
        if not client.mobile_phone.text or not match(r"\+\d{5,8}", client.mobile_phone.text):
            client.mobile_phone.error = True
            return False
        if not client.landline.text or not match(r"017\d{5,8}", client.landline.text):
            client.landline.error = True
            return False
        return True
