import subprocess
import atexit
import requests
import time

def start_ngrok():
    ngrok_process = subprocess.Popen(['ngrok', 'http', '5000'], stdout=subprocess.PIPE)
    atexit.register(ngrok_process.kill)
    
    
    time.sleep(2)  
    localhost_url = "http://localhost:4040/api/tunnels"
    
    for _ in range(10):  
        try:
            response = requests.get(localhost_url)
            response_data = response.json()
            
            
            if 'tunnels' in response_data and response_data['tunnels']:
                public_url = response_data['tunnels'][0]['public_url']
                print(f"ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:5000\"")
                return
            else:
                print("No tunnels found. Retrying...")
                
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

        time.sleep(1)  
    
    print("Failed to connect to ngrok. Please check ngrok's status.")
    exit(1)
