from sqlalchemy import or_
from .models import Client
from .session import Session


class Database:
    def __init__(self) -> None:
        pass

    def get_clients(self):
        with Session() as session:
            return session.query(Client).all()

    def get_filter_result(self, name: str, phone: str):
        with Session() as session:
            return session.query(Client).filter(
                Client.name.contains(name),
                or_(Client.mobile_phone.contains(phone),
                    Client.landline.contains(phone))
            ).all()

    def add_client(self, client: Client):
        with Session() as session:
            session.add(client)
            session.commit()

    def delete_clients(self, account_numbers: list[str]):
        with Session() as session:
            num_deleted = session.query(Client)\
                .where(Client.account_number.in_(account_numbers))\
                .delete()
            session.commit()
            print(f"Deleted {num_deleted} clients")
            return num_deleted
