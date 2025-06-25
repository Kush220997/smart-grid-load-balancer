from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Gauge
import threading
import time

app = Flask(__name__)
substation_load = Gauge('substation_load', 'Current active charging sessions')

active_sessions = 0

@app.route('/begin_charging', methods=['POST'])
def begin_charging():
    global active_sessions
    active_sessions += 1
    substation_load.set(active_sessions)
    threading.Thread(target=simulate_charge_process).start()
    return jsonify({"result": "Charging started"}), 200

def simulate_charge_process():
    global active_sessions
    time.sleep(10)
    active_sessions -= 1
    substation_load.set(active_sessions)

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
