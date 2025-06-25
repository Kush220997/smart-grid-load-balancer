import requests
import time

for i in range(50):
    response = requests.post("http://localhost:6000/initiate_energy_transfer")
    print(f"Request {i+1}: {response.json()}")
    time.sleep(0.2)
