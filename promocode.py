# Класс промокод

class Promocode():
    def __init__(self, promocode_id, users_who_used, percent):
        self._promocode_id = promocode_id
        self._users_who_used = users_who_used
        self._percent = percent

    @property
    def promocode_id(self):
        return self._promocode

    @property
    def users_who_used(self):
        return self._users_who_used

    @property
    def percent(self):
        return self._percent

    @promocode_id.setter
    def promocode_id(self, new_id):
        self._promocode_id = new_id

    @users_who_used.setter
    def users_who_used(self, new_users_list):
        self._users_who_used = new_users_list

    @percent.setter
    def percent(self, new_percent):
        self._percent = new_percent

    def add_user_who_used(self, user):
        self._users_who_used += [user]

    def available(self, client):
        for i in range(len(self._users_who_used)):
            if client == self._users_who_used[i]:
                return False
        return True
