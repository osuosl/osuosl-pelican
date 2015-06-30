import os
import urlparse
import smtplib
import redis
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from werkzeug.formparser import parse_form_data
from email.mime.text import MIMEText

class Forms(object):

    def __init__(self, config):
        print "in __init__"
        self.redis = redis.Redis(config['redis_host'], config['redis_port'])
        self.url_map = Map([
            Rule('/', endpoint='request_hosting')
        ])

    def dispatch_request(self, request):
        print "in dispatch_request"
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return(self, 'on_' + endpoint)(request, **values)
        except HTTPException, e:
            return e

    def on_request_hosting(self, request):
        print "in on_request_hosting"
        print request
        if request.method == 'POST':
            form_data = request.form
            print form_data
            send_email(form_data)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(redis_host='localhost', redis_port=6379, with_static=True):
    app = Forms({
        'redis_host':       redis_host,
        'redis_port':       redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static': os.path.join(os.path.dirname(__file__), 'static')
        })
    return app


if __name__ == '__main__':
    print "in request_handler.py"
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 8000, app, use_debugger=True, use_reloader=True)
