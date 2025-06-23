from flask import Flask, request, jsonify
import requests as rq

app = Flask(__name__)

@app.route('/ev_charge', methods=['POST'])
def req_chg():
    r = rq.post("http://lb_svc:7000/assign")
    return r.json(), r.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)