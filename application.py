import url
import tornado.web
import os

settings = {'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "statics"),
            'cookie_secret': "bZJc2s2bQLKoR6Gkj2/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            'xsrf_cookies': True,
            'login_url': '/login',
}

app = tornado.web.Application(
    handlers=url.urls,
    **settings
)
