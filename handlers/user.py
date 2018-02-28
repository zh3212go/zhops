import tornado.web
from util.mysql import select_table
from handlers.base import BaseHandler


class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = tornado.escape.json_decode(self.current_user)
        user_infos = select_table(table="users", column="*", condition="username", value=username)
        self.render("user.html", users=user_infos)
