import os

#need to sign S3 policy
import base64
import hmac, sha

from flask import Flask
from flask import request
from flask import Response
from flask import render_template

app = Flask(__name__)

@app.route("/sign_auth")
def sign_auth():
    to_sign = request.args.get('to_sign', '')
    signature = base64.b64encode(hmac.new(os.environ.get('AWS_SECRET_KEY'), to_sign, sha).digest())
    resp = Response(signature)
    resp.headers['Content-Type'] = 'text/html'
    return resp

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
