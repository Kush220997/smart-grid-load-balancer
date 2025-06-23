import requests as rq
import time

for i in range(50):
    res = rq.post("http://localhost:6000/ev_charge")
    print(f"Request {i+1}: {res.json()}")
    time.sleep(0.2)