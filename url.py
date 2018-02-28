from handlers.index import IndexHandler
from handlers.login import LoginHandler
from handlers.user import UserHandler

urls = [
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/user', UserHandler),
]