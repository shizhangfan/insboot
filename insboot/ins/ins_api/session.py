from .constants import Constans
from .request import Request

class Session():

    def __init__(self, device, storage, proxy):
        self.device = device
        self.storage = storage
        self.proxy = proxy

    def login(self, session, username, password):
        request = Request(session)