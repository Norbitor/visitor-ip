from flask import Flask, Response, jsonify, request

app = Flask(__name__)

past_ips = set()

@app.route("/")
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
def history():
    return jsonify(list(past_ips))

