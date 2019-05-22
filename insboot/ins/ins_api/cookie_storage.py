class CookieStorage(object):

    def __init__(self, cookie_storage):
        self.storage = cookie_storage

    @property
    def store(self):
        return self.storage

    @store.setter
    def store(self, storage):
        self.storage = storage

    def get_cookie_value(self, name):
        self.storage.find
