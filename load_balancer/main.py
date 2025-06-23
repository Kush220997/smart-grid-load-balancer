from flask import Flask, request, jsonify
import requests as rq

app = Flask(__name__)
subs = ['http://sub1:5000', 'http://sub2:5000']

def get_ld(url):
    try:
        res = rq.get(f"{url.replace(':5000', ':8000')}/metrics")
        for line in res.text.split('\n'):
            if 'evs' in line and not line.startswith('#'):
                return float(line.split()[-1])
    except:
        return float('inf')
    return float('inf')

@app.route('/assign', methods=['POST'])
def assign_sub():
    min_ld = min(subs, key=get_ld)
    res = rq.post(f"{min_ld}/begin")
    return res.json(), res.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)