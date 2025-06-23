from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Gauge
import threading
import time

app = Flask(__name__)
evs = Gauge('evs', 'EVs being charged')
n = 0

@app.route('/begin', methods=['POST'])
def begin():
    global n
    n += 1
    evs.set(n)
    threading.Thread(target=sim).start()
    return jsonify({"msg": "Charging started"}), 200

def sim():
    global n
    time.sleep(10)
    n -= 1
    evs.set(n)

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)