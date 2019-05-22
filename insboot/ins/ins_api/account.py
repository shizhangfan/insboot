from .request import Request


class Account:

    def get_by_id(self, session, id):
        request = Request(session)
        request.set_method('GET')
        request.set_resource('userInfo', {id: id})
        request.send()

