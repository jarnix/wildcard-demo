import os
from flask import Flask, request, make_response


app = Flask(__name__)


@app.route('/healthz')
def healthz():
    return 'OK'


@app.route('/')
def hello():
    body = u'remote address: %s\nx-forwarded-for: %s\nhostname: %s\npod ip: %s\npod name: %s\nnode name: %s' % (
        request.remote_addr, request.headers.get('X-Forwarded-For'), request.host,
        os.environ.get('POD_IP'), os.environ.get('POD_NAME'), os.environ.get('NODE_NAME'))
    resp = make_response(body)
    resp.headers['Content-Type'] = 'text/plain'
    return resp
