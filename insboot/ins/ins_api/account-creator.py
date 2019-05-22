import re
from .session import Session
from .request import Request


class AccountCreator(object):

    def __init__(self, session, operation_type):
        if not isinstance(session, Session):
            raise Exception("AccountCreator needs valid session as first argument")
        self.session = session
        if ['phone', 'email'].index(operation_type) < 1:
            raise Exception("AccountCreator class needs either phone or email as type")
        self.type = operation_type

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, username):
        username = username.lower()
        if not username or re.match(r'/^[a-z0-9\._]{1,50}$/', username):
            raise Exception("invalid username " + username)
        self.username = username
        return self

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name
        return self

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self.password = password
        return self


class AccountPhoneCreator(AccountCreator):

    def __init__(self, session):
        super(session, 'phone')

    @property
    def phone(self):
        return self.phone

    @phone.setter
    def phone(self, phone):
        if not re.match(r'/^([0-9\(\)\/\+ \-]*)$/', phone):
            raise Exception("Invalid phone")

        self.phone = phone
        return self

    def create(self):
        request = Request(self.session)
        request.set_method('POST')
        request.resource('registrationSMSCode')
        request.set

