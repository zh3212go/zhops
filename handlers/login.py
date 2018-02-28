import tornado.web
from util.mysql import select_table, select_columns
from handlers.base import BaseHandler


class LoginHandler(BaseHandler):
    def get(self):
        usernames = select_columns(table="users", column="username")
        one_user = usernames[0][0]
        self.render("login.html", user=one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = select_table(table="users", column="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.set_current_user(username)
                self.write(username)
            else:
                self.write("-2")
        else:
            self.write("-1")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")


class ErrorHandler(BaseHandler):
    def get(self):
        self.render("error.html")
