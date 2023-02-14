from flask import Flask, Response, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri='memory://',
)

past_ips = set()

@app.route("/")
@limiter.limit("1/second")
def caller_ip():
    '''
    Returns the caller's IP address in the format specified by user in
    the Accept header. If Accept header is not specified or is not supported,
    returns the IP address in plain text.
    '''
    ip = request.remote_addr
    past_ips.add(ip)
    accept_header = request.accept_mimetypes.best_match(['application/json', 'application/xml', 'text/html', 'text/plain'])
    if accept_header == 'application/json':
        return jsonify({'ip': ip})
    elif accept_header == 'application/xml':
        return Response(f'<?xml version="1.0" encoding="UTF-8"?><ip>{ip}</ip>', mimetype='application/xml')
    elif accept_header == 'text/html':
        return Response(f'<p>{ip}</p>', mimetype='text/html')
    else:
        return Response(ip, mimetype='text/plain')

@app.route("/history")
@limiter.limit("10/minute")
def history():
    return jsonify(list(past_ips))

