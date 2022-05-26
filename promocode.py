# Класс промокод
from uuid import uuid4, UUID
from typing import List


class Promocode:
    def __init__(self, percent: int):
        self.promocode_id: UUID = uuid4()
        self._users_who_used: List[UUID] = []
        self.percent = percent

    @property
    def users_who_used(self):
        return self._users_who_used

    @users_who_used.setter
    def users_who_used(self, new_users_list: List[UUID]):
        self._users_who_used = new_users_list

    def add_user_who_used(self, user: UUID) -> None:
        self._users_who_used += [user]

    def available(self, client: UUID) -> bool:
        if client in self._users_who_used:
            return False
        return True
