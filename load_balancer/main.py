from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
SUBSTATION_ENDPOINTS = ['http://substation1:5000', 'http://substation2:5000']

def query_load(substation_url):
    try:
        metrics_url = substation_url.replace(':5000', ':8000') + '/metrics'
        response = requests.get(metrics_url)
        for line in response.text.split('\n'):
            if 'substation_load' in line and not line.startswith('#'):
                return float(line.split(' ')[-1])
    except:
        return float('inf')
    return float('inf')

@app.route('/assign_substation', methods=['POST'])
def assign_substation():
    selected = min(SUBSTATION_ENDPOINTS, key=query_load)
    response = requests.post(f"{selected}/begin_charging")
    return response.json(), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
