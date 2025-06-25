from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/initiate_energy_transfer', methods=['POST'])
def initiate_energy_transfer():
    response = requests.post("http://load_balancer:7000/assign_substation")
    return response.json(), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
